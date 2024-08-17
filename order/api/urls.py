from django.urls import path, include
from rest_framework.routers import DefaultRouter
from order.api.views import OrderViewSet, OrderItemViewSet

router = DefaultRouter()
router.register("orders", OrderViewSet, basename="order")
router.register("orderitems", OrderItemViewSet, basename="orderitem")

urlpatterns = [
    path('', include(router.urls)),
]
