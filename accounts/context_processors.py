from django.contrib.auth.decorators import login_required
from .models import TuberProfile



def tuberprofile(request):
    all={}
    if request.user.is_authenticated and request.user.is_tuber:
        tuber=TuberProfile.objects.filter(user_id=request.user.id)
        if tuber:
            all['tuber']= tuber[0]
    
    return all
    