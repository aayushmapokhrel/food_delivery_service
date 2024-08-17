from django.contrib import admin
from home.models import Home


# Register your models here.
@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ["image"]
