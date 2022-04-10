"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import stat
from django.contrib import admin
from django.urls import include, path
from api import views
from base import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework import routers

from django.views.generic.base import TemplateView

# router = routers.DefaultRouter()
# router.register(r'users', views.UserDetails)
# router.register(r'groups', views.GroupDetails)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showHome, name = 'home'),
    path('signup/',views.showSignUp, name = 'signup'),
    path('signin/', views.showSignIn, name = 'signin'),
    path('build/', views.showBuildPage, name = 'build'),
    path('recommend/', views.showRecommendedPage, name = 'recommend'),
    path('cpu/', views.get_cpu, name = 'cpu'),
    path('gpu/', views.get_gpu, name = 'gpu'),
    path('motherboard/', views.get_motherboard, name='motherboard'),
    path('psu/', views.get_psu, name='psu'),
    path('memory/', views.get_ram, name='memory'),
    path('storage/', views.get_storage, name='storage'),
    path('case/', views.get_case, name='case'),
    path('liquidCooling/', views.get_liquidCool, name='liquidCooling'),
    path('airCooling/', views.get_airCool, name='airCooling'),
   

    # path('', views.home_view),
    # path('', TemplateView.as_view(template_name='home.html'), name="home"),
    # path('', include(router.urls)),
   
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
]

urlpatterns += staticfiles_urlpatterns()