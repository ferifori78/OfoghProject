from django.db import models
from django.contrib.gis.db import models
# Create your models here.
class NetworkConfiguration(models.Model):
    name = models.CharField(max_length=100)
    width = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name


class Penalty(models.Model):
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
    network = models.ForeignKey('NetworkConfiguration', on_delete=models.CASCADE)
    penalty_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Penalty for {self.driver.name}"