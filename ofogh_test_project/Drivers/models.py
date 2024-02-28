from django.db import models
from django.contrib.auth.models import User, AbstractUser


# driver model
class Driver(AbstractUser):
    id = models.AutoField(primary_key=True, unique=True, null=False, blank=False, auto_created=True)
    name = models.CharField(max_length=100)
    national_code = models.CharField(max_length=10, unique=True)
    age = models.IntegerField()
    total_toll_paid = models.FloatField(default=0)
    car = models.OneToOneField('Car', on_delete=models.CASCADE, related_name='driver_car')

    REQUIRED_FIELDS = ['national_code']


class Car(models.Model):
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE, related_name='car_driver')
    load_valume = models.FloatField(null=True, blank=True, default=0)
    length = models.FloatField(null=True, blank=True, default=0)
    color = models.CharField(max_length=100)
    TYPES = (
        ('small', 'Small'),
        ('big', 'Big'),
    )
    type = models.CharField(max_length=5, choices=TYPES)
    car_tag = models.CharField(max_length=10)
    location = models.PointField(srid=4326)
