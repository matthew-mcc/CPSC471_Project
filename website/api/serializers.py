#from django.contrib.auth.models import User, Group
from base.models import *
from rest_framework import serializers






#https://www.django-rest-framework.org/tutorial/quickstart/



# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups',]

#         #fields = '__all__'
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']



#convert instances of objects into data types the response object can understand



class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipient
        fields = '__all__'


class CPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPU
        fields = '__all__'

class GPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPU
        fields = '__all__'

class MotherBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotherBoard
        fields = '__all__'

class PowerSupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerSupply
        fields = '__all__'

class MemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Memory
        fields = '__all__'

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'

class AirCoolingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirCooling
        fields = '__all__'

class LiquidCoolingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiquidCooling
        fields = '__all__'

