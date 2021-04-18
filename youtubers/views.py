from django.shortcuts import render
from .models import Youtubers
from django.shortcuts import get_object_or_404
from accounts.models import Account,TuberProfile


# Create your views here.

# for search box # to manage all search box(home page , search page , youtuber page) from one place and call this fun from there views fun
def searchbox(request,youtubers):
    city_search          =TuberProfile.objects.values_list('city',flat=True).distinct()   # It returnds LIST
    camera_type_search   =TuberProfile.objects.values_list('camera_type',flat=True).distinct()
    category_search      =TuberProfile.objects.values_list('category',flat=True).distinct()
    

    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            youtubers=youtubers.filter(description__icontains=keyword)
           
    # for search fields which on search page

    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            youtubers=youtubers.filter(city__iexact=city)
            print(youtubers)

    if 'camera_type' in request.GET:
        camera_type=request.GET['camera_type']
        if camera_type:
            youtubers=youtubers.filter(camera_type__iexact=camera_type)
    
    if 'category' in request.GET:
        category=request.GET['category']
        if category:
            youtubers=youtubers.filter(category__iexact=category)


    data={
        'youtubers' : youtubers,
        'city_search' : city_search,
        "camera_type_search" : camera_type_search,
        "category_search" : category_search
    }

    return data



def youtubers(request):
    youtubers=TuberProfile.objects.order_by('-updated_date')

    # data={
    #     'youtubers': youtubers
    # }

    data=searchbox(request,youtubers)

    return render(request, 'youtubers/youtubers.html',data)


def youtubers_detail(request,user_id):

    youtuber=get_object_or_404(TuberProfile,pk=user_id)
    data={
        "youtuber":youtuber
    }
    
    return render(request, 'youtubers/youtuber_detail.html',data)


def search(request):
    youtubers=TuberProfile.objects.order_by("-updated_date")

    # city_search=Youtubers.objects.values_list('city',flat=True).distinct()   # It returnds LIST
    # camera_type_search=Youtubers.objects.values_list('camera_type',flat=True).distinct()
    # category_search=Youtubers.objects.values_list('category',flat=True).distinct()
    

    # if 'keyword' in request.GET:
    #     keyword=request.GET['keyword']
    #     if keyword:
    #         youtubers=youtubers.filter(description__icontains=keyword)

    # # for search fields which on search page

   
    # if 'city' in request.GET:
    #     city=request.GET['city']
    #     if city:
    #         youtubers=youtubers.filter(city__iexact=city)
   
    # if 'camera_type' in request.GET:
    #     camera_type=request.GET['camera_type']
    #     if camera_type:
    #         youtubers=youtubers.filter(camera_type__iexact=camera_type)
    
    # if 'category' in request.GET:
    #     category=request.GET['category']
    #     if category:
    #         youtubers=youtubers.filter(category__iexact=category)
    


    # data={
    #     'youtubers' : youtubers,
    #     'city_search' : city_search,
    #     "camera_type_search" : camera_type_search,
    #     "category_search" : category_search
    # }
    data=searchbox(request,youtubers)
    
    return render(request, 'youtubers/search.html',data)