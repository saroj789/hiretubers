from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import logout
#from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

from hiretubers.models import Hiretuber
from .decoretors import unauthenticated_user
from .models import Account,TuberProfile,gettuber_by_user

# Create your views here.

@unauthenticated_user
def login(request):
    # if request.user.is_authenticated:   # removed bz we use our decorators 
    #     return redirect('home')
    if request.method=='POST':
        #print(request.POST)
        email=request.POST['email']
        password=request.POST['password']
        is_tuber=bool(int(request.POST['is_tuber'])  )                                                  # form always gives you data in str form
        user=auth.authenticate(request,email=email,password=password)      # this object is available for all django templates by defaults
          
          
                                                                                            # we can use User object  to chechk user is logged in or not
        if user is not None and is_tuber==user.is_tuber :

            auth.login(request,user)
            #print(user.is_authenticated)
            #print('login',request.user)
            messages.success(request,'You are logged in')
            return redirect('dashboard')          

        else:
            messages.warning(request,'invalid crediantions')
            return redirect('login')

    return render(request,'accounts/login.html')



# we cannot create a func name as logout # becaause django has inbuilt logout fun
def logout_user(request):
    logout(request)
    return redirect('home')



@unauthenticated_user
def register(request):
    #print(request.user.is_authenticated)
    # if request.user.is_authenticated:                              # removed bz we use our decorators 
    #     return redirect('home')

    if request.method=='POST':
        print(request.POST)
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        user_name=request.POST['username']
        email=request.POST['email']
        is_tuber= bool(int(request.POST['is_tuber']))
        password=request.POST['password']
        confirm_password=request.POST['confirmpassword']


        if password==confirm_password and password!='':
            if  Account.objects.filter(username=user_name).exists():
                messages.warning(request,'username exists')
                return redirect('register')
            else:
                if Account.objects.filter(email=email).exists() :
                    messages.warning(request,'email already exists')
                    return redirect('register')
                else:
                    if is_tuber :
                        user=Account.objects.create_tuber(username=user_name,email=email,password=password)
                        type= 'Tuber'
                    else:
                        user=Account.objects.create_user(username=user_name,email=email,password=password)
                        type='User'
                    user.first_name=first_name
                    user.last_name=last_name
                    user.save()

                    messages.success(request,f"{type} Account created successfuly")
                    return redirect('login')

        else:
            messages.warning(request,'password do not match')
            return redirect('register')


    return render(request,'accounts/register.html')


@login_required(login_url='login')
def dashboard(request):
    
    sent_hirerequests=Hiretuber.objects.filter(user_id=request.user.id).order_by('-created_date').order_by('status')       # request.user is logged in user. if not logged in then it- AnnonymousUser
    data={'sent_hirerequests':sent_hirerequests}                                  # sent_hire_req
    
    if request.user.is_tuber:
        received_hire_req=Hiretuber.objects.filter(tuber_id=request.user.id ).order_by('-created_date').order_by('status')
        data['received_hirerequests']=received_hire_req
        #print(received_hire_req)          
    #print(data)                             
    return render(request,'accounts/dashboard.html',data)



@login_required(login_url='login')
def profile(request):
    data={}
          
    if request.method=='POST':

        #print(request.POST)
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        #user_name=request.POST['username']                        # disable inputs are not posted
        #email=request.POST['email']
        #is_tuber= bool(int(request.POST['is_tuber']))

        if request.FILES:
            profile_image=request.FILES['profile_image']
            request.user.profile_image=profile_image


        request.user.first_name=first_name
        request.user.last_name=last_name
        

        request.user.save()


        if request.user.is_tuber :

            video_url=request.POST['video_id']
            city=request.POST['city']
            crew=request.POST['crew']
            subs_count=request.POST['subs_count']
            camera_type=request.POST['camera_type']
            
            height=request.POST['height']
            price=request.POST['price']
            age=request.POST['age']
            category=request.POST['category']
            description=request.POST['description']
            announcement=request.POST['announcement']
            
            tuber=TuberProfile.objects.get_or_create(user_id=request.user.pk)[0]
          
            #tuber=gettuber_by_user(request.user)
            #print(announcement,tuber,request.user.pk) 
            
            
            tuber.video_url=video_url
            tuber.city=city
            tuber.crew=crew
            tuber.subs_count=subs_count
            tuber.camera_type=camera_type
            tuber.height=height
            tuber.price=price
            tuber.age=age
            tuber.category=category
            tuber.description=description
            tuber.announcement=announcement         

            tuber.save()
            
        messages.success(request,'profile updated successfully') 
        return render(request,'accounts/profileform.html')     

    else :
                                      
        return render(request,'accounts/profileform.html')




