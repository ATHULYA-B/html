from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    return render(request,'base.html')

def signup(request):
    if request.method =='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('pass1')
        password2=request.POST.get('cpass1')
        if password1==password2:
            if User.objects.filter(username=username,email=email).exits():
                messages.info(request,'username already exists!!!!!')
                print("already have")
            else:
              new_user=User.objects.create_user(username,email,password1)
              new_user.save()
              return redirect('user_login')
        else:
           print('wrong password')
    return render(request,'signup.html')
