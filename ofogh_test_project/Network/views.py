from django.shortcuts import render
from requests import Response
from rest_framework import generics
from rest_framework.views import APIView

from ofogh_test_project.Drivers.models import Driver
from ofogh_test_project.Network.models import Penalty, NetworkConfiguration
from ofogh_test_project.Network.serializers import PenaltySerializer


# Create your views here.
class BigCarPenaltyListAPIView(generics.ListAPIView):
    serializer_class = PenaltySerializer

    def get_queryset(self):
        return Penalty.objects.filter(driver__car__type='big', penalty_count__gt=0)


class PenaltyCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        driver_id = request.data.get('driver_id')
        network_id = request.data.get('network_id')
        network_width = NetworkConfiguration.objects.get(id=network_id).width
        driver_car_type = Driver.objects.get(id=driver_id).car.type
        if driver_car_type == 'big' and network_width > 20:
            penalty, created = Penalty.objects.get_or_create(driver_id=driver_id, network_id=network_id)
            if not created:
                penalty.penalty_count += 1
                penalty.save()
            return Response({'message': 'Penalty applied successfully'})
        return Response({'message': 'No penalty applied'})
