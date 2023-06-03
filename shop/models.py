from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=500, default=None, null=True)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)
    book_available = models.BooleanField(default=False)
    is_pdf = models.BooleanField(default=False)
    is_physical = models.BooleanField(default=False)
    is_ebook = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    stars = models.IntegerField(default=3)
    review = models.CharField(max_length=512, null=False)


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)  # type: ignore

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()  # type: ignore
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def cart_total(self):
        orderitems = self.orderitem_set.all()  # type: ignore
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def cart_count(self):
        orderitems = self.orderitem_set.all()  # type: ignore
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0, null=False, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity  # type: ignore
        return total


class UserDetail(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
