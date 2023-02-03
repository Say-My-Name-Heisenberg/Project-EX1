from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View
from .forms import RegForm,LogForm
from django.contrib import messages
from .models import Staff

# # Create your views here.
# def log(req):
#     if req.method=="GET":
#         return render(req,"login.html")
#     elif req.method=="POST":
#         print(req.POST)
#         user=req.POST.get("uname")
#         password=req.POST.get("pswd")
#         return HttpResponse ("username:"+user+"<br>Password:"+password)



# class LogView(View):
#     def get(self,req,*args,**kwargs):
#         return render (req,"login.html")
#     def post(self,req,*arga,**kwargs):
#         user=req.POST.get("uname")
#         password=req.POST.get("pswd")
#         return HttpResponse ("username:"+user+"<br>Password:"+password) 

# def registration(reg):
#     password=reg.POST.get("pswd")
#     cpassword=reg.POST.get("cpswd")
#     if reg.method=="GET":
#         return render(reg,"registration.html")
#     elif password!=cpassword:
#         return HttpResponse("PAssword doeen't match")
#     elif reg.method=="POST":
#         print(reg.POST)
#         first_name=reg.POST.get("fname")
#         last_name=reg.POST.get("lname")
#         mail=reg.POST.get("email")
#         user=reg.POST.get("uname")
#         password=reg.POST.get("pswd")
#         return HttpResponse ("NAME:"+first_name+" "+last_name+"<br>Email:"+mail+"<br>username:"+user+"<br>Password:"+password)
        
# class Registration(View):
#     def get(self,reg,*args,**kwargs):
#         return render(reg,"registration.html")
#     def post(self,reg,*args,**kwargs):
#         password=reg.POST.get("pswd")
#         cpassword=reg.POST.get("cpswd")
#         if reg.method=="GET":
#             return render(reg,"registration.html")
#         elif password!=cpassword:
#             return HttpResponse("PAssword doeen't match")
#         elif reg.method=="POST":
#             print(reg.POST)
#             first_name=reg.POST.get("fname")
#             last_name=reg.POST.get("lname")
#             mail=reg.POST.get("email")
#             user=reg.POST.get("uname")
#             password=reg.POST.get("pswd")
#             return HttpResponse ("NAME:"+first_name+" "+last_name+"<br>Email:"+mail+"<br>username:"+user+"<br>Password:"+password)

class RegView(View):
    def get(self,reg,*args,**kwargs):
        form = RegForm()
        return render(reg,"registration.html",{"form":form})
    def post(self,req,*args,**kwargs):
        form_data = RegForm(data=req.POST)
        if form_data.is_valid():
            fn=form_data.cleaned_data.get("first_name")
            ln=form_data.cleaned_data.get("last_name")
            exp=form_data.cleaned_data.get("experience")
            mail=form_data.cleaned_data.get("email")
            un=form_data.cleaned_data.get("username")
            psw=form_data.cleaned_data.get("password")
            Staff.objects.create(first=fn,last=ln,exp=exp,mail=mail,username=un,password=psw)
            messages.success(req,"Registration Sucessfull")
            return redirect ("Home")
        else:
            messages.error(req,"Registration Failed!")
            return render(req,"registration.html",{"form":form_data})

class LogView(View):
    def get(self,reg,*args,**kwargs):
        form = LogForm()
        return render(reg,"login.html",{"form":form})

class StaffView(View):
    def get (self,req,*args,**kwargs):
        res=Staff.objects.all()
        form = StaffView()
        return render (req,"Staff list.html",{"data":res})

        
class MainHome(View):
    def get(self,reg,*args,**kwargs):
        return render (reg,"main_home.html")

