from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class AddView(View):
    def get(self,req,*args,**kwargs):
        return render (req,"add.html")
    def post(self,req,*args,**kwargs):
        n1=req.POST.get("x")
        n2=req.POST.get("y")
        res=int(n1)+int(n2)
        return render (req,"add.html",{"data":res})


class SubView(View):
    def get(self,req,*args,**kwargs):
        return render (req,"sub.html")
    def post(self,req,*args,**kwargs):
        n1=req.POST.get("x")
        n2=req.POST.get("y")
        res=int(n1)-int(n2)
        return render (req,"sub.html",{"data":res})


class MulView(View):
    def get(self,req,*args,**kwargs):
        return render (req,"mul.html")
    def post(self,req,*args,**kwargs):
        n1=req.POST.get("x")
        n2=req.POST.get("y")
        res=int(n1)*int(n2)
        return render (req,"mul.html",{"data":res})

class DivView(View):
    def get(self,req,*args,**kwargs):
        return render (req,"div.html")
    def post(self,req,*args,**kwargs):
        n1=req.POST.get("x")
        n2=req.POST.get("y")
        res=int(n1)/int(n2)
        return render (req,"div.html",{"data":res})

class CountView(View):
    def get(self,req,*args,**kwargs):
        return render (req,"wordcount.html")
    def post(self,req,*args,**kwargs):
        t1=req.POST.get("x")
        x = t1.split()
        
        # b = []
        # c = {}
        # d = 0
        # for i in x:
        #     if i not in b:
        #         d = x.count(i)
        #         c.update({i: d})
        #         b.append(i)
        #     print(b)
        #     print(c)
        # return render (req,"wordcount.html",{"data":c})

        m = {}
        z = []
        for i in x:
            if i in z:
                continue
            z.append(i)
            m[i] = x.count(i)
        return render (req,"wordcount.html",{"data":m})

