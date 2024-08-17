from django.urls import path
from order.views import (
    OrderListView,
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView,
    OrderItemListView,
    OrderItemCreateView,
    OrderItemUpdateView,
    OrderItemDeleteView,
)

urlpatterns = [
    path("order/", OrderListView.as_view(), name="orders-list"),
    path("order/create/", OrderCreateView.as_view(), name="order-create"),
    path("order/<int:pk>/update/", OrderUpdateView.as_view(), name="order-update"),
    path("order/<int:pk>/delete/", OrderDeleteView.as_view(), name="order-delete"),
    path("orderitem/", OrderItemListView.as_view(), name="ordersitems-list"),
    path("orderitem/create/", OrderItemCreateView.as_view(), name="orderitem-create"),
    path(
        "orderitem/<int:pk>/update/",
        OrderItemUpdateView.as_view(),
        name="orderitem-update",
    ),
    path(
        "orderitem/<int:pk>/delete/",
        OrderItemDeleteView.as_view(),
        name="orderitem-delete",
    ),
]
