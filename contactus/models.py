from django.db import models

# Create your models here.
class Contactus(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    company=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.TextField(max_length=100)

    def __str__(self):
        return  self.name

 
