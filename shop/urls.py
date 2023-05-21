from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="homepage"),
    path("", views.store, name="store"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("update_item/", views.updateItem, name= "update_item"),
    path("<int:productId>", views.viewDetails, name='detail'),
    path("search/", views.searchResults, name='search_results'),
]
