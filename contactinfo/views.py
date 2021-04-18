from django.shortcuts import render,redirect
from .models import Contactinfo

#Create your views here.
def contactinfo(request):
     #contactinfo=Contactinfo.objects.order_by('-created_date')
     #print(contactinfo [0].header_phone)
     return redirect('/admin/contactinfo/contactinfo/add/')

    