from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView as DjangoLogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm, CustomUserLoginForm
from django.contrib import messages
from user.forms import UserBalanceForm
from django.views.generic.list import ListView
from user.models import UserBalance


class RegisterView(FormView):
    template_name = "registration/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("success-register")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class LoginView(FormView):
    template_name = "login/login.html"
    form_class = CustomUserLoginForm

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            if user.is_superuser and user.is_active:
                return redirect("restaurants-list")
            elif user.is_driver and user.is_active:
                return redirect("drivers-list")
            elif user.is_customer and user.is_active:
                return redirect("menusitems-list")
        return self.form_invalid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class SuccessRegisterView(TemplateView):
    template_name = "registration/success_register.html"


class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy("login")


class UserBalanceCreateView(LoginRequiredMixin, CreateView):
    model = UserBalance
    form_class = UserBalanceForm
    template_name = "user/balance_create.html"
    success_url = reverse_lazy("user-balance-list")

    def form_valid(self, form):
        user = form.cleaned_data["user"]
        if UserBalance.objects.filter(user=user).exists():
            messages.error(self.request, "User already has a balance entry.")
            return redirect(self.success_url)
        messages.success(self.request, "Balance created successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error creating balance.")
        return super().form_invalid(form)


class UserBalanceAddView(LoginRequiredMixin, UpdateView):
    model = UserBalance
    form_class = UserBalanceForm
    template_name = "user/balance_update.html"
    success_url = reverse_lazy("user-balance-list")

    def form_valid(self, form):
        user_balance = self.get_object()
        new_balance = form.cleaned_data["balance"]
        user_balance = self.add_balance(user_balance, new_balance)
        messages.success(self.request, "Balance updated successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error updating balance.")
        return super().form_invalid(form)


class UserBalanceListView(LoginRequiredMixin, ListView):
    model = UserBalance
    template_name = "user/balance_list.html"
    context_object_name = "user_balances"
