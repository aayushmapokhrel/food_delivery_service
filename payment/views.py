from django import forms
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView, ListView
from django.contrib import messages
from .models import Transaction
from user.models import UserBalance
from django.contrib.auth.models import User
import uuid
from django.http import HttpResponseRedirect


class TransactionForm(forms.ModelForm):
    receiver_username = forms.CharField(max_length=150)

    class Meta:
        model = Transaction
        fields = ["name", "amount", "transaction_type", "payment_method", "remarks"]


class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = "payment/create_transaction.html"

    def form_valid(self, form):
        user = self.request.user
        name = form.cleaned_data["name"]
        amount = form.cleaned_data["amount"]
        transaction_type = form.cleaned_data["transaction_type"]
        payment_method = form.cleaned_data["payment_method"]
        receiver_username = form.cleaned_data["receiver_username"]
        remarks = form.cleaned_data["remarks"]

        # Fetch the user's balance, return a 404 if not found
        user_balance = get_object_or_404(UserBalance, user=user)

        # Fetch the receiver user and their balance
        receiver = get_object_or_404(User, username=receiver_username)
        receiver_balance = get_object_or_404(UserBalance, user=receiver)

        # Check if it's an expense and the user has enough balance
        if transaction_type == Transaction.TransactionType.EXPENSE and amount > user_balance.balance:
            messages.error(self.request, "Insufficient balance!")
            return HttpResponseRedirect(self.request.path_info, status=400)

        # Create the transaction with a PENDING status
        transaction = Transaction.objects.create(
            name=name,
            transaction_type=transaction_type,
            amount=amount,
            transaction_id=uuid.uuid4(),
            user=user,
            receiver=receiver,
            status=Transaction.Transactionstatus.PENDING,
            payment_method=payment_method,
            remarks=remarks,
        )

        # Deduct from the user's balance if it's an expense
        if transaction_type == Transaction.TransactionType.EXPENSE:
            user_balance.balance -= amount
            receiver_balance.balance += amount  # Add to receiver's balance
            receiver_balance.save()
        else:
            user_balance.balance += amount
        user_balance.save()

        # Update the transaction status to COMPLETED
        transaction.status = Transaction.Transactionstatus.COMPLETED
        transaction.save()

        messages.success(self.request, "Transaction created successfully!")
        return redirect("transaction_list")


class TransactionListView(ListView):
    model = Transaction
    template_name = "payment/transaction_list.html"
    context_object_name = "transactions"

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_balance = UserBalance.objects.filter(user=self.request.user).first()
        context["balance"] = user_balance.balance if user_balance else 0
        return context
