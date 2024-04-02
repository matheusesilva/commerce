from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("add_listing", views.add_listing, name="add"),
    path("listings/<int:listing>", views.listing, name="listing"),
    path("listings/<int:listing>/wishlist", views.toggle_wishlist, name="toggle_wishlist"),
    path("my_wishlist", views.wishlist, name="wishlist"),
    path("categories", views.categories, name="categories"),
    path("<str:category>", views.category_page, name="category_page"),
    path("listings/<int:listing>/add_bid", views.add_bid, name="add_bid"),
    path("listings/<int:listing>/close_listing", views.close_listing, name="close_listing"),
    path("listings/<int:listing>/add_comment", views.add_comment, name="add_comment")
    ]
