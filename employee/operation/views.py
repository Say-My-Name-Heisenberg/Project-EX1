from django.shortcuts import render
from django.views.generic import View
from .forms import OpForm

# Create your views here.
class AddView(View):
    def get(self,req,*args,**kwargs):
        form = OpForm()
        return render (req,"add.html",{"form":form})
    def post(self,req,*args,**kwargs):
        form_data = OpForm(data=req.POST)
        if form_data.is_valid():
            num1=cleaned_data.get("num1")
            num2=cleaned_data.get("num2")
            res=int(num1)+int(num2)
            return render (req,"add.html",{"data":res})
        else:
            return render(req,"add.html",{"form":form_data})

class SubView(View):
    def get(self,req,*args,**kwargs):
        form = OpForm()
        return render (req,"sub.html",{"form":form})
    def post(self,req,*args,**kwargs):
        n1=req.POST.get("n1")
        n2=req.POST.get("n2")
        res=int(n1)-int(n2)
        return render (req,"sub.html",{"data":res})


class MulView(View):
    def get(self,req,*args,**kwargs):
        form = OpForm()
        return render (req,"mul.html",{"form":form})
    def post(self,req,*args,**kwargs):
        n1=req.POST.get("n1")
        n2=req.POST.get("n2")
        res=int(n1)*int(n2)
        return render (req,"mul.html",{"data":res})

class DivView(View):
    def get(self,req,*args,**kwargs):
        form = OpForm()
        return render (req,"div.html",{"form":form})
    def post(self,req,*args,**kwargs):
        n1=req.POST.get("n1")
        n2=req.POST.get("n2")
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

