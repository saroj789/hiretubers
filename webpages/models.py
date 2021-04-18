from django.db import models
from ckeditor.fields import RichTextField

class Team(models.Model):

    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    role=models.CharField(max_length=255)
    
    fb_link=models.CharField(max_length=255)
    insta_link=models.CharField(max_length=255)
    photo=models.ImageField(upload_to="webpages/team/%Y/%m/%d")
    created_date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.first_name



class Slider(models.Model):
    headline=models.CharField(max_length=255)
    subtitle=models.CharField(max_length=255)
    button_text=models.CharField(max_length=255)
    # button_url=models.URLField(default='#')
    photo=models.ImageField(upload_to='webpages/slider/%Y/%m/')
    created_date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.headline


class About(models.Model):
    headline=models.CharField(max_length=100, help_text='heading..')
    photo=models.ImageField(upload_to='webpages/about/%Y/')
    description=RichTextField()
    created_date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.headline