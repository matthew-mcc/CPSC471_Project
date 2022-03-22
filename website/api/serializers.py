from django.contrib.auth.models import User, Group
from itsdangerous import Serializer
from rest_framework import serializers

#https://www.django-rest-framework.org/tutorial/quickstart/


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups',]

        #fields = '__all__'
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']