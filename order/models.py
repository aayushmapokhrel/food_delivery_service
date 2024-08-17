from django.db import models
from user.models import User
from restaurant.models import MenuItem, Restaurant


class Order(models.Model):
    class Orderstatus(models.IntegerChoices):
        PENDING = 1, "PENDING"
        COMPLETED = 2, "COMPLETED"
        CANCELED = 3, "CANCELED"

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, blank=False)
    transaction_type = models.IntegerField(
        choices=Orderstatus.choices, default=Orderstatus.PENDING
    )
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name="orders_created"
    )

    def __str__(self):
        return "{0} - {1} - {2}".format(self.restaurant.name, self.id, self.full_name)

    def get_total_order_price(self):
        return sum(item.get_total_price() for item in self.order_items.all())



class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_items"
    )
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} x {1}".format(self.quantity, self.menu_item.name)

    def get_total_price(self):
        return self.quantity * self.menu_item.price
