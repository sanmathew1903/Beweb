from django.urls import path
from . import views

urlpatterns={
    
    path('',views.loginpage,name='loginpage'),
    path('index',views.index,name='index'),
    path('add',views.add,name='add'),
    path('display',views.display,name='display'),
    path('signin',views.signin,name='signin'),
    path('login',views.login,name='login'),
    path('login_info',views.login_info,name='login_info'),
    path('signin_info',views.signin_info,name='signin_info')
    
    
}