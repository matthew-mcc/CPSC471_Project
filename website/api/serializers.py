from django.contrib.auth.models import User, Group
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
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