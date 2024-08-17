from rest_framework import serializers
from home.models import Home


class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ["image"]