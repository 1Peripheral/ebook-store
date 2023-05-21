import json

from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import *


def index(request):
    context = {}
    return render(request, "shop/index.html", context)


def store(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "shop/store.html", context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}

        context = {"items": items, "oder": order}
    return render(request, "shop/checkout.html", context)


def cart(request):
    context = {}
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()  # type: ignore
        context = {"items": items, "order": order}
    else:
        return redirect("/login")

    return render(request, "shop/cart.html", context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]
    print("Action:", action)
    print("Product:", productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    OrderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == "add":
        OrderItem.quantity = orderItem.quantity + 1
    elif action == "remove":
        OrderItem.quantity = orderItem.quantity - 1

    OrderItem.save()

    if OrderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("Item was added", safe=False)


def login(request):
    context = {} 
    return render(request, "shop/login.html", context)