from django.urls import path
from restaurant.views import (
    RestaurantListView,
    RestaurantCreateView,
    RestaurantUpdateView,
    RestaurantDeleteView,
    MenuItemListView,
    MenuItemCreateView,
    MenuItemUpdateView,
    MenuItemDeleteView,
)

urlpatterns = [
    path("restaurant/", RestaurantListView.as_view(), name="restaurants-list"),
    path("restaurant/create/", RestaurantCreateView.as_view(), name="restaurant-create"),
    path("restaurant/<int:pk>/update/", RestaurantUpdateView.as_view(), name="restaurant-update"),
    path("restaurant/<int:pk>/delete/", RestaurantDeleteView.as_view(), name="restaurant-delete"),
    path("menuitem/", MenuItemListView.as_view(), name="menusitems-list"),
    path("menuitem/create/", MenuItemCreateView.as_view(), name="menuitem-create"),
    path(
        "menuitem/<int:pk>/update/",
        MenuItemUpdateView.as_view(),
        name="menuitem-update",
    ),
    path(
        "menuitem/<int:pk>/delete/",
        MenuItemDeleteView.as_view(),
        name="menuitem-delete",
    ),
]
