import email
from tkinter import E
from django.shortcuts import render , redirect
from django.contrib.auth import login , logout , authenticate

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from users.models import CustomUser
from .forms import RegisterForm , LogInForm
# Create your views here.


def register(request):
    if request.method != 'POST':
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            new_user = form.save()
            login(request,new_user)
            messages.success(request, "Registration successful." )
            return redirect("app:home")
    return render(request,'users/register.html',{'form':form})

def LogInPage(request):
    if request.method == 'POST':
        form = LogInForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            user = CustomUser.objects.get(username=username,email=email,password=password)
            if user is not None:
                login(request,user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("app:home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = LogInForm()
    return render(request,'users/login.html',{'form':form})
    

def LogOutPage(request):
    logout(request)    
    return redirect("users:LogInPage")
  