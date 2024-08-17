from django.contrib import admin
from driver.models import Driver, Delivery


# Register your models here.
@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone_number","vehicle_type","vehicle_number","is_available","current_location","rating","created_at","updated_at"]
    search_fields = ["first_name-current_location"]


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ["delivery_address", "assigned_at", "delivered_at"]
    search_fields = ["delivery_address", "assigned_at"]
