from rest_framework.response import Response
from rest_framework.decorators import api_view

from base.models import Item
from .serializers import ItemSerializer




@api_view(['GET'])
def getData(request):
    #user = {'userid': 'Testuser1', 'email': 'testuser1@google.com'} <-- dummy data

    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def getPart(request):
    #user = {'userid': 'Testuser1', 'email': 'testuser1@google.com'} <-- dummy data

    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addPart(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)