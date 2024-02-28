from rest_framework import serializers
from .models import Penalty, NetworkConfiguration


class PenaltySerializer(serializers.ModelSerializer):
    driver_name = serializers.SerializerMethodField()

    class Meta:
        model = Penalty
        fields = ['driver_name', 'penalty_count']

    def get_driver_name(self, obj):
        return obj.driver.name