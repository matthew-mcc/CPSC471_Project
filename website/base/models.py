from django.db import models

# Create your models here.


#this seems to be where the data is stored?
class Item(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)



#trying to add part model

class Part(models.Model):

    name = models.CharField(max_length=50)
    price = models.IntegerField()