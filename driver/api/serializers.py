from rest_framework import serializers
from driver.models import Driver, Delivery


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"

    def create(self, validated_data):
        created_by = validated_data.pop('created_by', None)
        driver = Driver.objects.create(**validated_data)
        if created_by:
            driver.created_by = created_by
            driver.save()

        return driver


class DeliverySerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = "__all__"

    def create(self, validated_data):
        created_by = validated_data.pop('created_by', None)
        delivery = Delivery.objects.create(**validated_data)
        if created_by:
            delivery.created_by = created_by
            delivery.save()

        return delivery
