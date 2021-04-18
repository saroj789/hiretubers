from django.shortcuts import render,redirect
from .models import Contactus
from django.contrib import messages

# Create your views here.
def contact(request):
    
    if request.method=="POST":
      
        name=request.POST["name"]
        phone=request.POST["phone"]
        email=request.POST["email"]
        company=request.POST["company"]
        subject=request.POST["subject"]
        message=request.POST["message"]
        
        #TODO checking

        contactus=Contactus(name=name, phone=phone, email=email, company=company, subject=subject, message = message)
        contactus.save()
        messages.success(request,'Thank you for contacting us !')
        return redirect('contact')
    else:
        return redirect('contact') 