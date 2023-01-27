from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View
from .forms import RegForm,LogForm
from django.contrib import messages

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
        #    res="Registration Success"
        #    return render (req,"registration.html",{"data":res})
            uname=form_data.cleaned_data.get("username")
            uname=form_data.cleaned_data.get("username")
            uname=form_data.cleaned_data.get("username")
            messages.success(req,"Registration Sucessfull")
            return redirect ("Home")
        else:
            messages.error(req,"Registration Failed!")
            return render(req,"registration.html",{"form":form_data})

class LogView(View):
    def get(self,reg,*args,**kwargs):
        form = LogForm()
        return render(reg,"login.html",{"form":form})

class MainHome(View):
    def get(self,reg,*args,**kwargs):
        return render (reg,"main_home.html")

