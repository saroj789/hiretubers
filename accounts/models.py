from django.db import models
from django.contrib.auth.models import  BaseUserManager,AbstractBaseUser
from django.core.validators import RegexValidator
from ckeditor.fields import RichTextField
from datetime import datetime
from django.contrib import messages

#Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,password):
        if not email:
            raise ValueError("User must have email")
        if not username:
            raise ValueError("User must have username")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password):       
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password=password
            )
        
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True

        user.save( using =self._db)
        return user

    def create_tuber(self,email,username,password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password=password
            )
        
        user.is_tuber=True

        user.save( using =self._db)
        return user


def  get_profile_image_path(self,filename=None):
    #return f"profile_images/{self.id}/{'profile_image.png'}"
    return f"profile_image/{self.id}_{self.username}/{filename}"

def  get_default_profile_image():
    #return 'profile_images/profile.png'
    return f'profile_image/profile.png'


class Account(AbstractBaseUser):
    email           = models.EmailField(verbose_name='email' , unique=True,)
    username        = models.CharField(max_length=100,unique=True)
    password        = models.CharField(max_length=100)
    date_joined     = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login', auto_now=True)
    
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    profile_image   = models.ImageField(upload_to=get_profile_image_path , default =get_default_profile_image ,blank=True)
    hide_email      = models.BooleanField(default=True)

    is_tuber        = models.BooleanField(default=False)
    first_name      = models.CharField(max_length=100)
    last_name       = models.CharField(max_length=100)
    # name=models.CharField(max_length=100)
    # last_name=models.CharField(max_length=100)
    # phone_regex = RegexValidator( regex = r'^\d{10}$',message = "phone number should exactly be in 10 digits")
    # phone = models.CharField(max_length=255, validators=[phone_regex], blank = True, null=True)         # you can set it unique = True

    USERNAME_FIELD = 'email'        # for login # default userneme
    REQUIRED_FIELDS=['username']

    objects= MyAccountManager()

    def __str__(self):
        return self.username

    
    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f"profile_images/{self.pk}/"):]


    # required fun coustomusers
    def has_perm(self,perm,obj=None):
        return self.is_active
    
    def has_module_perms(self,app_label):
        return True

    def gettuber_by_user(user):
        if user.is_tuber:
            tuber=TuberProfile.objects.filter(user_id=user.id)
            print(tuber[0])
            if tuber is None:
                tuber[0]=None
            return tuber[0]

        messages.info(request,'You are not a TUBER !')       
        return None







def gettuber_by_user(user):
    if user.is_tuber:
        tuber=TuberProfile.objects.filter(user_id=user.id)
        if tuber is None:
            tuber[0]=None
        return tuber[0]

    messages.info(request,'You are not a TUBER !')       
    #return tuber[0]
    return None


# Create your models here.    
class TuberProfile(models.Model):
    user = models.OneToOneField(to=Account, on_delete=models.CASCADE,primary_key=True)
   

    crew_choices=(
        ('solo','solo'),
        ('small','small'),
        ('large','large'),       
    )

    camera_choices=(
        ('canon','canon'),
        ('nicon','nicon'),
        ('sony','sony'),
        ('red','red'),
        ('fuji','fuji'),
        ('panasonic','panasonic'),
        ('other','other')      
    )


    category_choices=(
        ('Film & Animation','Film & Animation'),
        ('Music','Music'),
        ('Pets & Animals','Pets & Animals'),
        ('Gaming','Gaming'),
        ('Comedy','Comedy'),
        ('People & Blogs','People & Blogs'),
        ('Cooking','Cooking'), 
        ('Education',"Education") ,
        ('Science & Technology', "Science & Technology'"), 
        ('Entertainment' , 'Entertainment') ,
        ('News & Politics' , "News & Politics" ),
        ('Travel & Events','Travel & Events'),
        ('other','other')   ,

    )


   
    price= models.IntegerField(default=1)
    
    video_url= models.CharField(max_length=255 , blank=True)  # assume someone gives it video id ,video id used to embed
    description= RichTextField(default='No descriptions')
    announcement= RichTextField(default='No announcement')
    city= models.CharField(max_length=255, blank=True)
    age= models.IntegerField(default=1)
    height=models.IntegerField( default=1)
    crew= models.CharField( choices=crew_choices ,max_length=255, blank=True)
    camera_type= models.CharField(choices=camera_choices ,max_length=255 ,blank=True)
    subs_count= models.CharField(max_length=255,default=0)
    category= models.CharField(choices=category_choices ,max_length=255 ,blank=True)
    is_featured= models.BooleanField(default=False)   # impartant
    updated_date=models.DateTimeField(default=datetime.now,blank=True )

    def __str__(self):
        return self.user.first_name



    camera_types_for_tuber = ['canon','nicon','sony','red','fuji','panasonic','other']
    crew_choices_for_tuber=[
        'solo',
        'small',
        'large',     
        ]
    categories_for_tuber = [
                                'Film & Animation',
                                    'Music',
                                    'Pets & Animals'
                                    'Gaming',
                                    'Comedy',
                                    'People & Blogs',
                                    'Cooking',
                                    'Education' ,
                                    'Science & Technology', 
                                    'Entertainment' , 
                                    'News & Politics' ,
                                    'Travel & Events',
                                    'other'
        ]
    

