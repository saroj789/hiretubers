from django.shortcuts import render
from .models import Slider,Team,About
from youtubers.models import Youtubers
from contactinfo.models import Contactinfo
from accounts.models import Account,TuberProfile


# Create your views here



def home(request):
    sliders = Slider.objects.all()
    data={'sliders': sliders}

    teams=Team.objects.all()
    data['teams']=teams

    #all_tubers=Youtubers.objects.order_by('-created_date')
    all_tubers=TuberProfile.objects.order_by('-updated_date')
    data['all_tubers']=all_tubers 

    #featured_youtubers = Youtubers.objects.order_by('-created_date').filter(is_featured=True)
    featured_youtubers = TuberProfile.objects.order_by('-updated_date').filter(is_featured=True)

    data['featured_youtubers']=featured_youtubers
    
      
    #print(data)
    return render(request, "webpages/home.html",data)


def about(request):

    teams=Team.objects.all()
    data={'teams':teams}
    
    abouts=About.objects.order_by('created_date')
    data['abouts']= abouts
    
    return render(request, "webpages/about.html",data)

def services(request): 
    return render(request, "webpages/services.html")


def contact(request):
    
    return render(request, "webpages/contact.html")