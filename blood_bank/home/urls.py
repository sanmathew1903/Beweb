from django.urls import path
from . import views

urlpatterns=[
    
    path('',views.loginpage,name='loginpage'),
    path('donor_add',views.donor_add,name='donor_add'),
    path('display',views.display,name='display')
    
]