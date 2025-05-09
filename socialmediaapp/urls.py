from django.urls import path 
from . import views 

urlpatterns = [
    path('register/',views.register,name='register'),
    path('',views.user_login,name='login'),
    path('home/',views.home,name='dashboard'),
    path('logout/',views.user_logout,name='logout'),
    path('post/',views.post,name='post'),
    path('own_post/',views.own_post,name='own_post')
]