from django.contrib import admin
from order.models import OrderItem, Order


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["full_name", "phone_number","country","town_or_city","street_address1","date"]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['quantity']
