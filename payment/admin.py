from django.contrib import admin
from payment.models import Transaction


# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['status']
    search_fields = ["status"]