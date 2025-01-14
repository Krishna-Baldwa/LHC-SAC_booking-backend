from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('/user/register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('/user/register/')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name)
                user.save();
                return redirect('/user/login/')
        else:
            print("password not matching")  
            return redirect('/user/register/')  
        
        


    else:

        return render(request,'register.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

    else:
        return render(request,'userlogin.html')

    user=auth.authenticate(username=username,password=password)    

    if user is not None:
        auth.login(request,user)
        return redirect("/")
    else:
        messages.info(request,"invalid login")    
        return redirect("/user/register/")

    




