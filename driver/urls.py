from django.urls import path
from driver.views import (
    DriverListView,
    DriverCreateView,
    DriverUpdateView,
    DriverDeleteView,
    DeliveryListView,
    DeliveryCreateView,
    DeliveryUpdateView,
    DeliveryDeleteView,
)

urlpatterns = [
    path("driver/", DriverListView.as_view(), name="drivers-list"),
    path("driver/create/", DriverCreateView.as_view(), name="driver-create"),
    path("driver/<int:pk>/update/", DriverUpdateView.as_view(), name="driver-update"),
    path("driver/<int:pk>/delete/", DriverDeleteView.as_view(), name="driver-delete"),
    path("delivery/", DeliveryListView.as_view(), name="deliverys-list"),
    path(
        "delivery/create/",
        DeliveryCreateView.as_view(),
        name="delivery-create"
        ),
    path(
        "delivery/<int:pk>/update/",
        DeliveryUpdateView.as_view(),
        name="delivery-update",
    ),
    path(
        "delivery/<int:pk>/delete/",
        DeliveryDeleteView.as_view(),
        name="delivery-delete",
    ),
]
