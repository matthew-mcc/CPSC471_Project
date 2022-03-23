# from msilib.schema import Class
# from django.shortcuts import render

# from django.contrib.auth.models import User, Group
# from rest_framework import viewsets, permissions   

# from api.serializers import UserSerializer
# from api.serializers import GroupSerializer

# # Create your views here.

# #THIS IS THE ENDPOINT SECTION


# class UserDetails(viewsets.ModelViewSet):

#     """
#     API "ENDPOINT" that allows for users to be viewed or edited
#     """

#     # This is from the quickstart guide
#     queryset = User.objects.all().order_by('username') #can be order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     #this is from tutorial
#     # def get(self, request, pk, format=None):
#     #     user = User.objects.get(pk=pk)
#     #     serializer = UserSerializer(user)
#     #     return Response(serializer.data)

# class GroupDetails(viewsets.ModelViewSet):

#     """
#     API endpoint that allows for groups to be viewed or edited
#     """

#     queryset = Group.objects.all().order_by()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]


# def home_view(request):

#     return render(request, "home.html")
