from django.shortcuts import render
from rest_framework import serializers, viewsets, generics
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from .models import Station
from .serializer import CarLocationSerializer
from ..Drivers.models import Car, Driver
from ..Drivers.serializers import DriverInfoSerializer


class SmallCarsWithin600mOfTollRoad1(generics.ListAPIView):
    serializer_class = CarLocationSerializer

    def get_queryset(self):
        toll_road_1 = Station.objects.get(name="Toll Road 1")
        small_cars = Car.objects.filter(type="small")
        cars_within_600m = [car.location for car in small_cars if car.location.distance(toll_road_1.location) < D(m=600)]
        return cars_within_600m


class DriversWithTollViolations(generics.ListAPIView):
    serializer_class = DriverInfoSerializer

    def get_queryset(self):
        # Assuming there is a field in the Driver model to track toll violations and their amount
        drivers_with_violations = Driver.objects.filter(toll_violation=True).order_by('violation_amount')
        return drivers_with_violations