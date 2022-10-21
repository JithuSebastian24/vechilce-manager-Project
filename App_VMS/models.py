from django.db import models

# Create your models here.

class VehiceDetails(models.Model):
    VehicleNum=models.CharField(max_length=20)
    Vehicletype=models.CharField(max_length=20)
    VehicleModel=models.CharField(max_length=20)
    VehicleDes=models.CharField(max_length=200)
