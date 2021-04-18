from django.urls import path
from . import views


urlpatterns = [
    path('hiretuber', views.hiretuber,name='hiretuber'),
    path('sent/<int:id>', views.sent_hirerequest,name='sent_hirerequest'),                 # we cant write only '<int:id>' for  both url b/z the it is then url match first pattern and run it wi
    path('received/<int:id>', views.received_hirerequest,name='received_hirerequest'),

    path('reqcancel/<int:hire_id>',views.cancel_hirereq,name='cancel_hirereq'),
    path('reqaccept/<int:hire_id>',views.accept_hirereq,name='accept_hirereq'),
    path('reqreject/<int:hire_id>',views.reject_hirereq,name='reject_hirereq'),
    


]