from order.models import Order, OrderItem
from django import forms


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = "__all__"

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
