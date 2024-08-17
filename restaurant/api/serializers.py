from rest_framework import serializers
from restaurant.models import MenuItem, Restaurant


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ["id", "name", "description", "price"]


class RestaurantSerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        exclude = ["created_by", "modified_by"]

    def get_menu_items(self, obj):
        return list(obj.menu_items.values_list("name", flat=True))
