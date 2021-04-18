from django.db import models
from django.utils import timezone
from datetime import datetime

from accounts.models import TuberProfile,Account
from django.conf import settings
# Create your models here.






class Hiretuber(models.Model):
    status_choices=(
        ('sent','sent'),
        ('received','received'),
        ('delivered','delivered'),
        ('accepted','accepted') ,
        ('rejected','rejected')

    )

    user_id=models.IntegerField( blank=True)
    sender=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='sender_user', blank=True,default=1)
    receiver=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='receiver_user', blank=True,default=1)
    print(sender)
    first_name=models.CharField(max_length=100 ,default="first_name")
    last_name=models.CharField(max_length=100 ,default="last_name")
    tuber_id=models.IntegerField()
    tuber_name=models.CharField(max_length=100)

    city=models.CharField(max_length=100)
    phone=models.IntegerField(blank=True)
    email=models.EmailField()
    state=models.CharField(max_length=100)
    message=models.TextField(blank=True)
    
    status=models.CharField(choices=status_choices, max_length=20,default='delivered')
    created_date=models.DateTimeField(blank=True, default=datetime.now)


    def __str__(self):
       return self.email

    def get_tuber_details_by_hiretuber(self):
        tuber_details=TuberProfile.objects.filter(user_id=self.tuber_id)[0]
       
        return tuber_details


        

# class HiredTubersList(models.Model):
#     user                    =   models.OneToOneField(settings.AUTH_USER_MODEL,related_name='user',on_delete=models.CASCADE)
#     sent_hired_list         =   models.ForeignKey("Hiretuber", on_delete=models.CASCADE , related_name='sent_hiretuber',blank=True)
#     received_hired_list     =   models.ForeignKey("Hiretuber",on_delete=models.CASCADE,related_name='received_hiretuber',blank=True)

#     def __str__(self):
#         return self.user.email


#     def add_hired(self,hireruber):
#         if self.user == hireruber.tuber_id:
#             self.received_hired_list.append(hireruber)
#             self.save()
#             hireruber.status='accepted'
        
#         if self.user == hireruber.user_id:
#             self.sent_hired_list.append(hireruber)
#             self.save()
