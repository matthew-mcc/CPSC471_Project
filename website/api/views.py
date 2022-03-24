from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from base.models import User
from .serializers import UserSerializer
#from website.api import serializers



""" POST -> Creates new records
    GET -> For reading records
    PUT -> Updating Specific Record
    DELETE -> Remove Specific Record
"""



class UserList(APIView):

    @api_view(['GET'])
    def getUsers(request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    @api_view(['POST'])
    def addUser(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class UserDetail(APIView):
    @api_view(['GET'])
    def getDetails(request, id):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

