from django.shortcuts import render
userlist=[]
# Create your views here.
def index(request):
    return render(request,'index.html')

def add(request):
    user=request.POST['username']
    pswd=request.POST['password']
    dict={user:pswd}
    userlist.append(dict)
    return render(request,'index.html')
    
def display(request):
    return render(request,'display.html',{'data':userlist})