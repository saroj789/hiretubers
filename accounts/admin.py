from django.contrib import admin
from django.utils.html import format_html
from .models import Account,TuberProfile
# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    def myphoto(self,object):
        return format_html('<img src="{}" width="40" />'.format(object.profile_image.url))

    list_display = ('email','username','myphoto','date_joined','last_login', 'is_tuber', 'is_staff','is_admin','is_superuser')
    search_fields=('email','username')
    readonly_fields= ('id','date_joined','last_login')
    list_filter=('is_tuber','is_admin','is_staff','is_superuser')


admin.site.register(Account,AccountAdmin)
admin.site.register(TuberProfile)