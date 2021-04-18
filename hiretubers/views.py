from django.shortcuts import render,redirect,HttpResponse
from .models import Hiretuber
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.models import TuberProfile

# @login_required(login_url='login') 
def hiretuber(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        tuber_id=request.POST['tuber_id']
        tuber_name=request.POST['tuber_name']
        city=request.POST['city']
        phone=request.POST['phone']
        email=request.POST['email']
        state=request.POST['state']
        message=request.POST['message']
        user_id=request.POST['user_id']

        receiver=TuberProfile.objects.filter(user_id=tuber_id)[0].user
      
        print("first_name",first_name,"last_name", last_name,"tuber_id", tuber_id,"tuber_name" ,tuber_name,"city" ,city ,"phone", phone,"email", email,"state", state,"message", message,"user_id", user_id,'receiver',receiver)
        # TODO: du all sanatization ( chacking msgs phone email etc validations )

        #hiretuber=Hiretuber()
        hiretuber=Hiretuber(sender=request.user ,receiver=receiver , user_id=user_id, first_name=first_name, last_name=last_name, tuber_id=tuber_id, tuber_name=tuber_name, city=city, phone=phone, email=email, state=state , message=message   )
       
        print(hiretuber.first_name)
        hiretuber.save()
        messages.success(request,'Thanks for reaching out!')
        return redirect('youtubers')
    else:
        return redirect('youtubers')
    
       

# sent and received hiretubers for dashboard(visit : go to the page , where show hiretuber details )


@login_required(login_url='login')
def sent_hirerequest(request,id):
    hirerequest=Hiretuber.objects.filter(id=id)[0]          # filter returns queryset but we need hiretuber obj
    
    data={'hirerequest':hirerequest}
    
    #tuber_details=TuberProfile.objects.filter(user_id=hirerequest.tuber_id)[0]
    tuber_details=hirerequest.get_tuber_details_by_hiretuber()
    data['tuber_details']=tuber_details      # TuberProfile obj

    return render(request, 'hiretubers/sent_hirerequest.html',data)


@login_required(login_url='login')
def received_hirerequest(request,id):
    hirerequest=Hiretuber.objects.filter(id=id)[0]          # filter returns queryset but we need hiretuber obj
    
    data={'hirerequest':hirerequest}
    #print(type(data['hirerequest']),data['hirerequest'].)
    tuber_details=hirerequest.get_tuber_details_by_hiretuber()
    data['tuber_details']=tuber_details 

    return render(request, 'hiretubers/received_hirerequest.html',data)





# for cancel accept and reject button on dashboard
@login_required(login_url='login')
def cancel_hirereq(request,hire_id):
    print(hire_id)
    hirereq=Hiretuber.objects.filter(id=hire_id)[0]
   
    print(hirereq)
    if hirereq.status=='accepted':
        return HttpResponse('You cannot cancel it because it acceped already')
    #hirereq.delete()
    
    return HttpResponse('Deleted successfully'+hirereq.tuber_name)


@login_required(login_url='login')
def accept_hirereq(request,hire_id):
    print(hire_id)
    hirereq=Hiretuber.objects.filter(id=hire_id)[0]
    if hirereq.status=='accepted':
        return HttpResponse('Already accepted')
    if hirereq.status=='rejected':
        return HttpResponse('rejected requests you can not accept it')
    hirereq.status='accepted'
    hirereq.save()
    
    print(hirereq)
    #hirereq.delete()
    
    return HttpResponse('Hire request of '+hirereq.first_name + "is "+hirereq.status)

@login_required(login_url='login')
def reject_hirereq(request,hire_id):
    print(hire_id)
    hirereq=Hiretuber.objects.filter(id=hire_id)[0]
    if hirereq.status=='rejected':
        return HttpResponse('Already rejected')
    if hirereq.status=='accepted':
        return HttpResponse('accepted requests you can not reject it')
    hirereq.status='rejected'
    hirereq.save()
    
    print(hirereq.status)
    #hirereq.delete()
    
    return HttpResponse(hirereq.status )