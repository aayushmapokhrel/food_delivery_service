from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, View
from django.contrib.auth.mixins import UserPassesTestMixin
from restaurant.models import Restaurant, MenuItem
from restaurant.forms import RestaurantForm, MenuItemForm
from django.shortcuts import get_object_or_404, redirect


class RestaurantRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class RestaurantListView(RestaurantRequiredMixin, ListView):
    model = Restaurant
    context_object_name = "restaurants"
    success_url = reverse_lazy("restaurants-list")

    def get_template_names(self):
        if self.request.user.is_superuser:
            return ["restaurant/restaurant_list.html"]
        elif self.request.user.is_staff:
            return ["restaurant/restaurant_list.html"]
        return []


class RestaurantCreateView(RestaurantRequiredMixin, CreateView):
    model = Restaurant
    form_class = RestaurantForm
    success_url = reverse_lazy("restaurants-list")

    def get_template_names(self):
        if self.request.user.is_superuser:
            return ["restaurant/restaurant_form.html"]
        elif self.request.user.is_staff:
            return ["restaurant/restaurant_form.html"]
        return []

    def form_valid(self, form):
        restaurant = form.save(commit=False)
        restaurant.created_by = self.request.user
        restaurant.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("restaurants-list")


class RestaurantUpdateView(RestaurantRequiredMixin, UpdateView):
    model = Restaurant
    form_class = RestaurantForm
    success_url = reverse_lazy("restaurants-list")

    def get_template_names(self):
        if self.request.user.is_superuser:
            return ["restaurant/restaurant_form.html"]
        elif self.request.user.is_staff:
            return ["restaurant/restaurant_form.html"]
        return []

    def form_valid(self, form):
        restaurant = form.save(commit=False)
        restaurant.modified_by = self.request.user
        restaurant.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("restaurants-list")


class RestaurantDeleteView(RestaurantRequiredMixin, View):
    success_url = reverse_lazy("restaurants-list")

    def post(self, request, pk, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, pk=pk)
        restaurant.delete()
        return redirect(reverse_lazy("restaurants-list"))


class MenuItemRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class MenuItemListView(MenuItemRequiredMixin, ListView):
    model = MenuItem
    context_object_name = "menuitems"
    success_url = reverse_lazy("menusitems-list")

    def get_template_names(self):
        if self.request.user.is_superuser:
            return ["menu/menuitem_list.html"]
        elif self.request.user.is_staff:
            return ["menu/menuitem_list.html"]
        return []


class MenuItemCreateView(MenuItemRequiredMixin, CreateView):
    model = MenuItem
    form_class = MenuItemForm
    success_url = reverse_lazy("menusitems-list")

    def get_template_names(self):
        if self.request.user.is_superuser:
            return ["menu/menuitem_form.html"]
        elif self.request.user.is_staff:
            return ["menu/menuitem_form.html"]
        return []

    def form_valid(self, form):
        menuitem = form.save(commit=False)
        menuitem.created_by = self.request.user
        menuitem.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("menusitems-list")


class MenuItemUpdateView(MenuItemRequiredMixin, UpdateView):
    model = MenuItem
    form_class = MenuItemForm
    success_url = reverse_lazy("menusitems-list")

    def get_template_names(self):
        if self.request.user.is_superuser:
            return ["menu/menuitem_form.html"]
        elif self.request.user.is_staff:
            return ["menu/menuitem_form.html"]
        return []

    def form_valid(self, form):
        menuitem = form.save(commit=False)
        menuitem.modified_by = self.request.user
        menuitem.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("menusitems-list")


class MenuItemDeleteView(MenuItemRequiredMixin, View):
    success_url = reverse_lazy("menusitems-list")

    def post(self, request, pk, *args, **kwargs):
        menuitem = get_object_or_404(MenuItem, pk=pk)
        menuitem.delete()
        return redirect(reverse_lazy("menusitems-list"))
