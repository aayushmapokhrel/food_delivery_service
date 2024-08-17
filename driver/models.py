from django.db import models
from user.models import User
from order.models import Order


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    vehicle_type = models.CharField(max_length=30)
    vehicle_number = models.CharField(max_length=15)
    is_available = models.BooleanField()
    current_location = models.CharField(max_length=255, blank=True, null=True)
    rating = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name


class Delivery(models.Model):
    class Deliverystatus(models.IntegerChoices):
        pending = (
            1,
            "Pending",
        )
        in_progress = (
            2,
            "In Progress",
        )
        completed = (
            3,
            "Completed",
        )
        failed = 4, "Failed"

    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    driver = models.ForeignKey(
        "Driver",
        on_delete=models.CASCADE,
    )
    delivery_address = models.CharField(max_length=255)
    delivery_status = models.IntegerField(choices=Deliverystatus.choices)
    assigned_at = models.DateTimeField()
    delivered_at = models.DateTimeField()

    def __str__(self):
        return f"Delivery for Order #{self.order.id} - {self.delivery_status}"


