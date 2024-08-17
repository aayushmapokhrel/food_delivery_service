from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, View
from django.contrib.auth.mixins import UserPassesTestMixin
from order.models import Order, OrderItem
from order.forms import OrderForm, OrderItemForm
from django.shortcuts import get_object_or_404, redirect


class OrderRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class OrderListView(OrderRequiredMixin, ListView):
    model = Order
    context_object_name = "orders"
    success_url = reverse_lazy("orders-list")

    def get_template_names(self):
        if self.request.user.is_superuser:
            return ["order/order_list.html"]
        elif self.request.user.is_staff:
            return ["order/order_list.html"]
        return []


class OrderCreateView(OrderRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("orders-list")

    def get_template_names(self):
        if self.request.user.is_superuser:
            return ["order/order_form.html"]
        elif self.request.user.is_staff:
            return ["order/order_form.html"]
        return []

    def form_valid(self, form):
        order = form.save(commit=False)
        order.created_by = self.request.user
        order.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("orders-list")


class OrderUpdateView(OrderRequiredMixin, UpdateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("orders-list")

    def get_template_names(self):
        if self.request.user.is_superuser:
            return ["order/order_form.html"]
        elif self.request.user.is_staff:
            return ["order/order_form.html"]
        return []

    def form_valid(self, form):
        order = form.save(commit=False)
        order.modified_by = self.request.user
        order.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("orders-list")


class OrderDeleteView(OrderRequiredMixin, View):
    success_url = reverse_lazy("orders-list")

    def post(self, request, pk, *args, **kwargs):
        order = get_object_or_404(Order, pk=pk)
        order.delete()
        return redirect(reverse_lazy("orders-list"))


class OrderItemRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class OrderItemListView(OrderItemRequiredMixin, ListView):
    model = OrderItem
    context_object_name = "ordersitems"
    success_url = reverse_lazy("ordersitem-list")

    def get_template_names(self):
        if self.request.user.is_superuser:
            return ["order/orderitem_list.html"]
        elif self.request.user.is_staff:
            return ["order/orderitem_list.html"]
        return []


class OrderItemCreateView(OrderItemRequiredMixin, CreateView):
    model = OrderItem
    form_class = OrderItemForm
    success_url = reverse_lazy("ordersitems-list")

    def get_template_names(self):
        if self.request.user.is_superuser:
            return ["order/orderitem_form.html"]
        elif self.request.user.is_staff:
            return ["order/ordeitem_form.html"]
        return []

    def form_valid(self, form):
        order = form.save(commit=False)
        order.created_by = self.request.user
        order.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("ordersitems-list")


class OrderItemUpdateView(OrderItemRequiredMixin, UpdateView):
    model = OrderItem
    form_class = OrderItemForm
    success_url = reverse_lazy("ordersitems-list")

    def get_template_names(self):
        if self.request.user.is_superuser:
            return ["order/orderitem_form.html"]
        elif self.request.user.is_staff:
            return ["order/orderitem_form.html"]
        return []

    def form_valid(self, form):
        order = form.save(commit=False)
        order.modified_by = self.request.user
        order.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("ordersitems-list")


class OrderItemDeleteView(OrderItemRequiredMixin, View):
    success_url = reverse_lazy("ordersitems-list")

    def post(self, request, pk, *args, **kwargs):
        orderitem = get_object_or_404(OrderItem, pk=pk)
        orderitem.delete()
        return redirect(reverse_lazy("ordersitems-list"))
