from django.shortcuts import render
from django.http import HttpResponse

userlist=[]
users=[]
# Create your views here.

def signin(request):
    return render(request,'signin.html')

def signin_info(request):
    username=request.POST['username']
    password=request.POST['password']
    dict={username:password}
    users.append(dict)
    return render(request,'loginpage.html')

def login(request):
    return render(request,'login.html')

def login_info(request):
    username=request.POST['username']
    password=request.POST['password']
    for i in users:
        for j in i:
            if j==username and i[j]==password:
                return render(request,'index.html')
    return HttpResponse("<html><body><h1>NO USER FOUND</h1></body></html>")



def loginpage(request):
    return render(request,'loginpage.html')

def index(request):
    return render(request,'index.html')

def add(request):

    name=request.POST['name']
    age=int(request.POST['age'])
    blood_type=request.POST['blood_type']

    dict={name:[age,blood_type]}
    print(dict)
    userlist.append(dict)
    return render(request,'index.html')
    
def display(request):
    return render(request,'display.html',{'data':userlist})