from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from auctions.models import Category, Listing, User, Bid, Comment
from django import forms
from decimal import Decimal
from django.db.models import Max

from .models import User

class AddListing (forms.Form):
    Title = forms.CharField(label="Title")
    Category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None)
    Initial_Price = forms.DecimalField(max_digits=6, decimal_places=2)
    Image = forms.URLField()
    Description = forms.CharField(max_length=300)

class PlaceBid (forms.Form):
    def __init__(self,listing, *args, **kwargs):
        super(PlaceBid,self).__init__(*args, **kwargs)
        product = Listing.objects.get(pk=listing)
        if product.max_bid > 0:
            min_value = product.max_bid
        else:
            min_value = product.initial_price
        self.fields['Value'] = forms.DecimalField(max_digits=6, decimal_places=2, label='', min_value = (min_value + Decimal(0.01)))

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
    
def index (request):
    listings = Listing.objects.filter(is_active = True)
    listings_won = Listing.objects.filter(winner=request.user.id)
    return render (request,"auctions/index.html", {
        "listings": listings,
        "listings_won": listings_won
    })

def listing (request,listing):
    is_wishlisted = False
    is_owner = False
    is_winner = False
    product = Listing.objects.get(pk=listing)
    comments = Comment.objects.filter(product=listing)
    if request.user.is_authenticated:
        user = User.objects.get(pk=request.user.id)
        if user.wishlisted.filter(pk=product.id):
            is_wishlisted = True
        if user == product.owner:
            is_owner = True
        if user == product.winner:
            is_winner = True

    return render (request, "auctions/listing.html", {
        "listing": product,
        "is_wishlisted": is_wishlisted,
        "is_owner": is_owner,
        "is_winner": is_winner,
        "comments": comments,
        "place_bid": PlaceBid(listing)
    })

def toggle_wishlist (request,listing):
    user = User.objects.get(pk=request.user.id)
    product = Listing.objects.get(pk=listing)
    if user in product.wishlist.all():
        product.wishlist.remove(user)
    else:
        product.wishlist.add(user)
    return HttpResponseRedirect(reverse('listing', args=(listing,)))

def categories (request):
    categories = Category.objects.all()
    return render (request, "auctions/categories.html", {
        "categories": categories
    })

def category_page (request,category):
    category = Category.objects.get(category=category)
    listings = Listing.objects.filter(category=category.id)
    return render (request, "auctions/category_page.html", {
        "category": category,
        "listings": listings
    })

def wishlist (request):
    user = User.objects.get(pk=request.user.id)
    listings = user.wishlisted.all()
    return render (request, "auctions/wishlist.html", {
        "wishlist": listings
    })

def add_listing (request):
    if request.method == "POST":
        form = AddListing(request.POST)
        if form.is_valid():
            new_listing = Listing.objects.create(
                title = form.cleaned_data["Title"],
                description = form.cleaned_data["Description"],
                initial_price = form.cleaned_data["Initial_Price"],
                category = form.cleaned_data["Category"],
                image = form.cleaned_data["Image"],
                owner = request.user,
                is_active = True
            )
    return render (request, "auctions/add.html", {
        "form": AddListing
    })

def add_bid (request,listing):
    if request.method == "POST":
        form = PlaceBid(listing,request.POST)
        if form.is_valid():
            new_bid = Bid.objects.create (
                product = Listing.objects.get(pk=listing),
                value = form.cleaned_data["Value"],
                buyer = request.user
            )
            product = Listing.objects.get(pk=listing)
            product.max_bid = form.cleaned_data["Value"]
            product.save()
    return HttpResponseRedirect(reverse('listing', args=(listing,)))

def close_listing (request,listing):
    product = Listing.objects.get(pk=listing)
    product.is_active = False
    highest_bid = Bid.objects.get(value=product.max_bid)
    product.winner = highest_bid.buyer
    product.save()
    return HttpResponseRedirect(reverse('listing', args=(listing,)))

def add_comment (request,listing):
    if request.method == "POST":
        new_comment = Comment.objects.create(
        product = Listing.objects.get(pk=listing),
        content = request.POST['comment'],
        user = request.user
        )
    return HttpResponseRedirect(reverse('listing', args=(listing,)))