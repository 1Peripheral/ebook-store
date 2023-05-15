from django.shortcuts import render
from django.http import JsonResponse
from .models import *


def index(request):
    context = {}
    return render(request, "shop/index.html", context)


def store(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "shop/store.html", context)


def checkout(request):
    context = {}
    return render(request, "shop/checkout.html", context)


def cart(request):
    context = {}
    return render(request, "shop/cart.html", context)


def updateItem(request):
    return JsonResponse('Item was added', safe=False)