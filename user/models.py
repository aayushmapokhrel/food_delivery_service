from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_restaurant = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_set",
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions_set",
        blank=True,
    )

    def __str__(self):
        return self.username


class UserBalance(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    balance = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username
