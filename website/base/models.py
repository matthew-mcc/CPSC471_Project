from django.db import models

# Create your models here.


# as per ER diagram
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    #dont really understand how to do primary keys...
    #userID = models.BigAutoField(primary_key=True)

class CPU(models.Model):
    model_name = models.CharField(max_length=50)
    power_usage = models.IntegerField()
    graphics = models.CharField(max_length=100)
    chipset = models.CharField(max_length=50)
    core_count = models.IntegerField()
    core_clock = models.CharField(max_length=20)
