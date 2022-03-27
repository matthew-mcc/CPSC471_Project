#api urls


from django.urls import path
from . import views


urlpatterns = [
    
    
    path('getUsers/', views.UserList.getUsers),
    path('addUser/', views.UserList.addUser),
    path('getUser/<int:id>', views.UserDetail.getDetails) #to access certain user do site/getUser/id
    

]