from restaurant.models import Restaurant, MenuItem
from django import forms


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = "__all__"

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
