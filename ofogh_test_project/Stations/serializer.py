from rest_framework import serializers
from ..Drivers.models import Car


class CarLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'location']