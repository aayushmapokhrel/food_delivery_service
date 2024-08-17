from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from user.models import User, UserBalance


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "is_restaurant",
            "is_customer",
            "is_driver",
        ]


class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )


class UserBalanceForm(forms.ModelForm):
    class Meta:
        model = UserBalance
        fields = ['user', 'balance']
        widgets = {
            'balance': forms.NumberInput(attrs={'step': '0.01'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_balance(self):
        balance = self.cleaned_data.get('balance')
        if balance < 0:
            raise forms.ValidationError("Balance cannot be negative.")


        return balance