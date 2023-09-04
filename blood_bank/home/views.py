from django.shortcuts import render
userlist=[]
# Create your views here.
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