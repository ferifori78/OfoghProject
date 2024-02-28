from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Driver
from .serializers import DriverRegisterSerializer, DriverInfoSerializer


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverRegisterSerializer

    # CRUD operations base on serialiazer
    # create a driver
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    # list all drivers
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    # update a driver
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    # delete a driver
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    # retrieve a driver
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class ElderlyDriverListAPIView(generics.ListAPIView):
    serializer_class = DriverInfoSerializer

    def get_queryset(self):
        return Driver.objects.filter(age__gt=70)


class BlueRedCarListAPIView(generics.ListAPIView):
    serializer_class = DriverInfoSerializer

    def get_queryset(self):
        # Assuming you want to retrieve all drivers and their associated blue and red cars
        drivers_with_blue_red_cars = Driver.objects.filter(car__color__in=['blue', 'red']).distinct()
        return drivers_with_blue_red_cars
