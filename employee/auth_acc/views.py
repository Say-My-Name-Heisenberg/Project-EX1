from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class Home_Page(View):
    def get(self,req):
        return render (req,"Homepage.html")