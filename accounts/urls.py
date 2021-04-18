from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login,name='login'),
    path('register', views.register,name='register'),
    path('logout', views.logout_user,name='logout'),    # we cannot create a func name as logout 
    path('dashboard', views.dashboard,name='dashboard'),      # becaause django has inbuilt logout fun
    path('profile',views.profile,name='profile'),
    
]