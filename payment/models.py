from django.db import models
from user.models import User


# Create your models here.
class Transaction(models.Model):
    class Transactionstatus(models.IntegerChoices):
        COMPLETED = 1, "COMPLETED"
        FAILURE = 2, "FAILURE"
        INITIATED = 3, "INITIATED"
        PENDING = 4, "PENDING"

    class PaymentMethod(models.IntegerChoices):
        ESEWA = 1, "ESEWA"
        KHALTI = 2, "KHALTI"
        ADMIN = 3, "ADMIN"

    class TransactionType(models.IntegerChoices):
        INCOME = 1, "INCOME"
        EXPENSE = 2, "EXPENSE"

    name = models.CharField(max_length=50, null=True, blank=True)
    transaction_type = models.IntegerField(
        choices=TransactionType.choices, default=TransactionType.INCOME
    )
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    transaction_id = models.UUIDField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    user_email = models.CharField(max_length=40, null=True, blank=True)
    status = models.IntegerField(
        choices=Transactionstatus.choices, default=Transactionstatus.PENDING
    )
    _from = models.CharField(max_length=100, null=True, blank=True)
    to = models.CharField(max_length=100, null=True, blank=True)
    payment_method = models.IntegerField(choices=PaymentMethod.choices)
    remarks = models.TextField(null=True, blank=True)
    receiver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="received_transactions")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
