import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render

from .models import *


def index(request):
    context = {}
    return render(request, "shop/index.html", context)


def store(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "shop/store.html", context)


@login_required(login_url="/accounts/login")
def checkout(request):
    context = {}
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()  # type: ignore
    else:
        items = []
        order = {"cart_total": 0, "cart_items": 0}

    context = {"items": items, "order": order}
    return render(request, "shop/checkout.html", context)


@login_required(login_url="/accounts/login")
def cart(request):
    context = {}
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()  # type: ignore
        context = {"items": items, "order": order}

    return render(request, "shop/cart.html", context)


def viewDetails(request, productId):
    print(productId)
    product = Product.objects.get(id=productId)
    reviews = product.review_set.all() #type: ignore
    context = {"product": product, "reviews": reviews}
    return render(request, "shop/detail.html", context)


def searchResults(request):
    context = {}
    if request.method == 'POST':
        search_query = request.POST['search_query']
        items = Product.objects.filter(name__icontains=search_query)
        context = {'items' : items}
    return render(request, "shop/search_results.html", context)

def postReview(request, productId):
    if request.method == 'POST':
        review_text = request.POST['review']
        product = Product.objects.get(id=productId)
        review = Review(user=request.user, product=product, review=review_text)
        review.save()
        return redirect(viewDetails, productId)
    return redirect(viewDetails, productId)



def updateItem(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]

    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)  # type: ignore

    if action == "add":
        orderItem.quantity += 1
    elif action == "remove":
        orderItem.quantity -= 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("Item was added", safe=False)

    