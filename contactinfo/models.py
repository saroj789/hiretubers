from django.db import models

class Contactinfo(models.Model):
    header_email=models.EmailField()
    header_phone=models.IntegerField()
    footer_fb_link=models.CharField(max_length=100,blank=True,default='https://www.facebook.com/')
    footer_insta_link=models.CharField(max_length=100,blank=True ,default='https://www.instagram.com/')
    footer_twitter_link=models.CharField(max_length=100,blank=True ,default='https://www.twitter.com/')
    footer_youtube_link=models.CharField(max_length=100,blank=True ,default='https://www.youtube.com/')
    created_date=models.DateTimeField(auto_now_add=True)
   




    def __str__(self):
        return self.header_email

