from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Donors
from django.views.decorators.cache import never_cache

# Create your views here.

'''def signin(request):
   return render(request,'register.html')

def signin_info(request):
    username=request.POST['username']
    password=request.POST['password']
    dict={username:password}
    users.append(dict)
    return render(request,'index.html')


def login_info(request):
    username=request.POST['username']
    password=request.POST['password']
    for i in users:
        for j in i:
            if j==username and i[j]==password:
                return render(request,'donor.html')
    return HttpResponse("<html><body><h1>NO USER FOUND</h1></body></html>")'''



@never_cache
def index(request):
    return render(request,'index.html')

@never_cache
def donor(request):
    return render(request,'donor.html')


@never_cache
def donor_add(request):
    
    if request.method=='POST':
            name=request.POST['name']
            age=int(request.POST['age'])
            blood_type=request.POST['blood_type']
            en=Donors(D_name=name,D_age=age,D_blood=blood_type)
            en.save()
            return redirect('donor_add')
            
    else:
    
        return render(request,'donor.html')
        
    
@never_cache
def display(request):
    #donor_data=Donors.objects.all()
    return render(request,'display.html',{'data':Donors.objects.all()})