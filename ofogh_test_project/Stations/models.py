from django.db import models
from django.contrib.gis.db import models

class Station(models.Model):
    name = models.CharField(max_length=100)
    toll_per_cross = models.IntegerField()
    location = models.PointField(srid=4326)

    def __str__(self):
        return self.name