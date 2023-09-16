from django.urls import path
from . import views

urlpatterns=[
    
    path('',views.loginpage,name='loginpage'),
    path('index',views.index,name='index'),
    path('add',views.add,name='add'),
    path('display',views.display,name='display')
    
]