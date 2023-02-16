from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View
from .forms import RegForm,LogForm,RegModelForm
from django.contrib import messages
from .models import Staff
from django.utils.decorators import method_decorator


#==== Decorator ====#
def signin_required(fn):
    def wrapper(req,*args,**kwargs):
        if req.user.is_authenticated:
            return fn(req,*args,**kwargs)
        else:
            return redirect ("Homepage")
    return wrapper

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

# def reqistration(req):
#     password=req.POST.get("pswd")
#     cpassword=req.POST.get("cpswd")
#     if req.method=="GET":
#         return render(req,"reqistration.html")
#     elif password!=cpassword:
#         return HttpResponse("PAssword doeen't match")
#     elif req.method=="POST":
#         print(req.POST)
#         first_name=req.POST.get("fname")
#         last_name=req.POST.get("lname")
#         mail=req.POST.get("email")
#         user=req.POST.get("uname")
#         password=req.POST.get("pswd")
#         return HttpResponse ("NAME:"+first_name+" "+last_name+"<br>Email:"+mail+"<br>username:"+user+"<br>Password:"+password)
        
# class reqistration(View):
#     def get(self,req,*args,**kwargs):
#         return render(req,"reqistration.html")
#     def post(self,req,*args,**kwargs):
#         password=req.POST.get("pswd")
#         cpassword=req.POST.get("cpswd")
#         if req.method=="GET":
#             return render(req,"reqistration.html")
#         elif password!=cpassword:
#             return HttpResponse("PAssword doeen't match")
#         elif req.method=="POST":
#             print(req.POST)
#             first_name=req.POST.get("fname")
#             last_name=req.POST.get("lname")
#             mail=req.POST.get("email")
#             user=req.POST.get("uname")
#             password=req.POST.get("pswd")
#             return HttpResponse ("NAME:"+first_name+" "+last_name+"<br>Email:"+mail+"<br>username:"+user+"<br>Password:"+password)

# ========================================================================================

# class reqView(View):
#     def get(self,req,*args,**kwargs):
#         form = reqForm()
#         return render(req,"reqistration.html",{"form":form})
#     def post(self,req,*args,**kwargs):
#         form_data = reqForm(data=req.POST)
#         if form_data.is_valid():
#             fn=form_data.cleaned_data.get("first_name")
#             ln=form_data.cleaned_data.get("last_name")
#             exp=form_data.cleaned_data.get("experience")
#             mail=form_data.cleaned_data.get("email")
#             un=form_data.cleaned_data.get("username")
#             psw=form_data.cleaned_data.get("password")
#             Staff.objects.create(first=fn,last=ln,exp=exp,mail=mail,username=un,password=psw)
#             messages.success(req,"reqistration Sucessfull")
#             return redirect ("Home")
#         else:
#             messages.error(req,"reqistration Failed!")
#             return render(req,"reqistration.html",{"form":form_data})

# using modelform

class RegView(View):
    def get(self,req,*args,**kwargs):
        form=RegModelForm()
        return render(req,"reqistration.html",{"form":form})    
    def post(self,req,*args,**kwargs):
        form_data = RegModelForm(data=req.POST,files=req.FILES)
        if form_data.is_valid():
            form_data.save()
            messages.success(req,"reqistration Sucessfull")
            return redirect ("Home")
        else:
            messages.error(req,"reqistration Failed!")
            return render(req,"reqistration.html",{"form":form_data})

class LogView(View):
    def get(self,req,*args,**kwargs):
        form = LogForm()
        return render(req,"login.html",{"form":form})

@method_decorator(signin_required,name='dispatch')
class StaffView(View):
    def get (self,req,*args,**kwargs):
        if req.user.is_authenticated:
            res=Staff.objects.all()
            return render (req,"Staff list.html",{"data":res})
        else:
            return redirect("Homepage")

@method_decorator(signin_required,name='dispatch')
class StaffDelete(View):
    def get (self,req,*args,**kwargs):
        id=kwargs.get("sid")
        staff=Staff.objects.get(id=id)
        staff.delete()
        messages.success(req,"Staff Removed")
        return redirect("Staff")
    
# class StaffEdit(View):
#     def get(self,req,*args,**kwargs):
#         id=kwargs.get("sid")
#         staff=Staff.objects.get(id=id)
#         form = reqForm(initial={"first_name":staff.first,"last_name":staff.last,"experience":staff.exp,"email":staff.mail,"username":staff.username,"password":staff.password})
#         return render(req,"Edit Staff.html",{"form":form})
#     def post(self,req,*args,**kwargs):
#         form_data=reqForm(data=req.POST)
#         if form_data.is_valid():
#             fn=form_data.cleaned_data.get("first_name")
#             ln=form_data.cleaned_data.get("last_name")
#             exp=form_data.cleaned_data.get("experience")
#             mail=form_data.cleaned_data.get("email")
#             un=form_data.cleaned_data.get("username")
#             psw=form_data.cleaned_data.get("password")
#             id=kwargs.get("sid")
#             staff=Staff.objects.get(id=id)
#             staff.first=fn
#             staff.last=ln
#             staff.exp=exp
#             staff.mail=mail
#             staff.password=psw
#             staff.username=un
#             staff.save()
#             messages.success(req,"Staff Details Updated")
#             return redirect ('Staff')
#         else:
#             messages.success(req,"Staff Details Updation failed")
#             staff=Staff.objects.get(id=id)
#             return render (req,"Edit Staff.html",{"form":form_data})


@method_decorator(signin_required,name='dispatch')       
class StaffEdit(View):
    def get(self,req,*args,**kwargs):
        id=kwargs.get("sid")
        staff=Staff.objects.get(id=id)
        form=RegModelForm(instance=staff)
        return render(req,"Edit Staff.html",{"form":form})
    def post(self,req,*args,**kwargs):
        id=kwargs.get("sid")
        staff=Staff.objects.get(id=id)
        form_data=RegModelForm(data=req.POST,files=req.FILES)
        if form_data.is_valid():
            form_data.save()
            messages.success(req,"Staff Details Updated")
            return redirect ('Staff')
        else:
            messages.success(req,"Staff Details Updation failed")
            return render (req,"Edit Staff.html",{"form":form_data})

@method_decorator(signin_required,name='dispatch')           
class MainHome(View):
    def get(self,req,*args,**kwargs):
        user=req.user
        return render (req,"main_home.html",{"name":user})

