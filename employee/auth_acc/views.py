from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.

class Home_Page(View):
    def get(self,req):
        return render (req,"Homepage.html")
    

class SignupView(View):
    def get(self,reg,*args,**kwargs):
        form=RegistrationForm()
        return render(reg,"Sign Up.html",{"form":form})    
    def post(self,req,*args,**kwargs):
        form_data = RegistrationForm(data=req.POST,files=req.FILES)
        if form_data.is_valid():
            form_data.save()
            messages.success(req,"User Registration Sucessfull")
            return redirect ("Homepage")
        else:
            messages.error(req,"User Registration Failed!")
            return render(req,"Sign Up.html",{"form":form_data})


class SigninView(View):
    def get(self,reg,*args,**kwargs):
        form =LoginForm()
        return render(reg,"Sign In.html",{"form":form})
    def post (self,req,*args,**kwargs):
        form_data=LoginForm(data=req.POST)
        if form_data.is_valid():
            un=form_data.cleaned_data.get("username")
            psw=form_data.cleaned_data.get("password")
            user=authenticate(req,username=un,password=psw)
            if user:
                messages.success(req,"LOgin SucCess")
                return redirect("Home")
            else:
                messages.error(req,"Login Failed")
                return redirect("Sign In")
        else:
            return render (req,"Sign In.html",{"form":form_data})


class LogOut(View):
    def get(self,req):
        return redirect("Sign in")