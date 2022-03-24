#from django.contrib.auth.models import User, Group
from base.models import User
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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

