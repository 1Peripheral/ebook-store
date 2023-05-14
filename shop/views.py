from django.shortcuts import render


def store(request):
    context = {}
    return render(request, "shop/store.html", context)


def checkout(request):
    context = {}
    return render(request, "shop/checkout.html", context)


def cart(request):
    context = {}
    return render(request, "shop/cart.html", context)
