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
