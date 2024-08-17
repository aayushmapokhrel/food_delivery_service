from django.db import models
from user.models import User


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='manuitem_images/', null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    image = models.ImageField( upload_to='restaurant_images/', null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    menu_items = models.ManyToManyField(MenuItem, related_name='restaurants')
    is_active = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User, null=True, on_delete=models.RESTRICT, related_name="restaurant_created_at"
    )
    modified_by = models.ForeignKey(
        User,
        null=True,
        on_delete=models.RESTRICT,
        related_name="restaurant_modified_at",
    )
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return self.name
