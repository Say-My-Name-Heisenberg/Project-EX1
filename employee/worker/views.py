from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
def index(req):
    return HttpResponse("<h2>Adios Amigo</h2>")

# def home(req):
#     name="sree"
#     items = ["chrome","firefox","opera","zzz"]
#     val=0
#     return render (req,"home.html",{"var":name,"data":items,"val":val})



class Homeview(View):
    def get(self,req,*args,**kwargs):
        return render (req,"home.html")
