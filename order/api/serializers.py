from rest_framework import serializers
from order.models import Order, OrderItem
from restaurant.models import Restaurant, MenuItem


class OrderItemSerializer(serializers.ModelSerializer):
    menu_item = serializers.PrimaryKeyRelatedField(queryset=MenuItem.objects.all())

    class Meta:
        model = OrderItem
        fields = ["menu_item", "quantity"]


class OrderSerializer(serializers.ModelSerializer):
    restaurant = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all())
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            "restaurant",
            "full_name",
            "phone_number",
            "country",
            "town_or_city",
            "street_address1",
            "street_address2",
            "date",
            "order_items",
        ]

    def create(self, validated_data):
        order_items_data = validated_data.pop("order_items")
        order = Order.objects.create(**validated_data)

        for item_data in order_items_data:
            OrderItem.objects.create(order=order, **item_data)

        return order

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        order_items = OrderItem.objects.filter(order=instance)
        representation["order_items"] = OrderItemSerializer(order_items, many=True).data
        return representation

    def validate(self, data):
        restaurant = data.get("restaurant")
        order_items = data.get("order_items")

        if not restaurant:
            raise serializers.ValidationError("Restaurant must be specified.")

        for item_data in order_items:
            menu_item = item_data["menu_item"]
            if menu_item not in restaurant.menu_items.all():
                raise serializers.ValidationError(
                    f"Menu item {menu_item.name} is not available in the selected restaurant."
                )

        return data
