from django.contrib import admin
from restaurant.models import Restaurant, MenuItem


# Register your models here.
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "price"]
    search_fields = ["name"]


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "phone_number", "opening_time", "closing_time"]
    search_fields = ["name", "address"]
