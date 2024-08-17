from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User, UserBalance


class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "is_staff",
        "is_restaurant",
        "is_customer",
        "is_driver",
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("is_restaurant", "is_customer", "is_driver")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("is_restaurant", "is_customer", "is_driver")}),
    )


class UserBalanceAdmin(admin.ModelAdmin):
    list_display = ("user", "balance")


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserBalance, UserBalanceAdmin)
