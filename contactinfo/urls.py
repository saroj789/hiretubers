# to handle header and footer of base html and contactinfo on contact pagefrom django.urls import path


from django.urls import path
from . import views


urlpatterns = [
    path('', views.contactinfo,name='contactinfo'),


]