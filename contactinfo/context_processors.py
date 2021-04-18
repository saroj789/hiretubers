
#return value of this avail for all templates

from datetime import datetime
from .models import Contactinfo

def contactinfo(request):
    contact=Contactinfo.objects.order_by('-created_date')
    contact={}
    
    if not contact:
        contact[0]={
            'header_email': 'help@mytuber.com' ,
            'header_phone':'1498989898'  ,
            'footer_fb_link': 'https://www.facebool.com/' ,
            'footer_insta_link':  'https://www.instagram.com/',
            'footer_twitter_link':  'https://www.twitter.com/',
            'footer_youtube_link' : 'https://www.youtube.com/'  ,
            'created_date':   datetime.now ,

        }
    data={"contactinfo" : contact[0]}
    return data