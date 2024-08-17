from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, View
from django.contrib.auth.mixins import UserPassesTestMixin
from driver.models import Driver, Delivery
from driver.forms import DriverForm, DeliveryForm
from django.shortcuts import get_object_or_404, redirect


class DriverRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_driver or self.request.user.is_superuser


class DriverListView(DriverRequiredMixin, ListView):
    model = Driver
    context_object_name = "drivers"
    success_url = reverse_lazy("drivers-list")


    def get_template_names(self):
        if self.request.user.is_superuser:
            return ["driver/driver_list.html"]
        elif self.request.user.is_staff:
            return ["driver/driver_list.html"]
        return []


class DriverCreateView(DriverRequiredMixin, CreateView):
    model = Driver
    form_class = DriverForm
    success_url = reverse_lazy("drivers-list")

    def get_template_names(self):
        if self.request.user.is_superuser:
            return ["driver/driver_form.html"]
        elif self.request.user.is_staff:
            return ["driver/driver_form.html"]
        return []

    def form_valid(self, form):
        driver = form.save(commit=False)
        driver.created_by = self.request.user
        driver.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("drivers-list")


class DriverUpdateView(DriverRequiredMixin, UpdateView):
    model = Driver
    form_class = DriverForm
    success_url = reverse_lazy("drivers-list")

    def get_template_names(self):
        if self.request.user.is_superuser:
            return ["driver/driver_form.html"]
        elif self.request.user.is_staff:
            return ["driver/driver_form.html"]
        return []

    def form_valid(self, form):
        driver = form.save(commit=False)
        driver.modified_by = self.request.user
        driver.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("drivers-list")


class DriverDeleteView(DriverRequiredMixin, View):
    success_url = reverse_lazy("drivers-list")

    def post(self, request, pk, *args, **kwargs):
        driver = get_object_or_404(Driver, pk=pk)
        driver.delete()
        return redirect(reverse_lazy("drivers-list"))


class DeliveryRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class DeliveryListView(DeliveryRequiredMixin, ListView):
    model = Delivery
    context_object_name = "deliverys"
    success_url = reverse_lazy("deliverys-list")

    def get_template_names(self):
        if self.request.user.is_superuser:
            return ["delivery/delivery_list.html"]
        elif self.request.user.is_staff:
            return ["delivery/delivery_list.html"]
        return []


class DeliveryCreateView(DeliveryRequiredMixin, CreateView):
    model = Delivery
    form_class = DeliveryForm
    success_url = reverse_lazy("deliverys-list")

    def get_template_names(self):
        if self.request.user.is_superuser:
            return ["delivery/delivery_form.html"]
        elif self.request.user.is_staff:
            return ["delivery/delivery_form.html"]
        return []

    def form_valid(self, form):
        delivery = form.save(commit=False)
        delivery.created_by = self.request.user
        delivery.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("deliverys-list")


class DeliveryUpdateView(DeliveryRequiredMixin, UpdateView):
    model = Delivery
    form_class = DeliveryForm
    success_url = reverse_lazy("deliverys-list")

    def get_template_names(self):
        if self.request.user.is_superuser:
            return ["delivery/delivery_form.html"]
        elif self.request.user.is_staff:
            return ["delivery/delivery_form.html"]
        return []

    def form_valid(self, form):
        delivery = form.save(commit=False)
        delivery.modified_by = self.request.user
        delivery.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("deliverys-list")


class DeliveryDeleteView(DeliveryRequiredMixin, View):
    success_url = reverse_lazy("deliverys-list")

    def post(self, request, pk, *args, **kwargs):
        delivery = get_object_or_404(Delivery, pk=pk)
        delivery.delete()
        return redirect(reverse_lazy("deliverys-list"))
