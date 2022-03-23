#api urls


from django.urls import path
from . import views


urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem),
    path('getPart/', views.getPart)
]