from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.category}"

class Listing(models.Model):
    title = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)
    description = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='listings', null=True)
    image = models.URLField()
    initial_price = models.DecimalField(max_digits=6, decimal_places=2)
    max_bid = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    addDate = models.DateField(auto_now_add=True)
    wishlist = models.ManyToManyField(User, related_name="wishlisted",blank=True)
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='listings_won', blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

class Bid(models.Model):
    product = models.ForeignKey(Listing, on_delete=models.CASCADE, default='', related_name='bids')
    value = models.DecimalField(max_digits=6, decimal_places=2)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids')
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
   
                            
class Comment(models.Model):
    product = models.ForeignKey(Listing, on_delete=models.CASCADE, default='')
    content = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
