from driver.models import Driver, Delivery
from django import forms


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = "__all__"

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = "__all__"

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
