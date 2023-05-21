from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="homepage"),
    path("store/", views.store, name="store"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("update_item/", views.updateItem, name= "update_item"),
    path("login/", views.login, name= "login"),
]
