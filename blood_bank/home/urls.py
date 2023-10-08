from django.urls import path
from . import views

urlpatterns=[
    
    path('',views.index,name='index'),
    path('donor_add',views.donor_add,name='donor_add'),
    path('display',views.display,name='display')
    
]