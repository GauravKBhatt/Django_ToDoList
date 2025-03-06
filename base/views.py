from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class home(View):
    def get(self,request,*args,**kwargs):
        return render(request,'base/home.html')

class item(View):
    def get(self,request,*args,**kwargs):
        return render(request,'base/item.html')

class create(View):
    def get(self,request,*args,**kwargs):
        return render(request,'base/createupdate.html')

class update(View):
    def get(self,request,*args,**kwargs):
        return render(request,'base/createupdate.html')

class delete(View):
    def get(self,request,*args,**kwargs):
        return render(request,'base/delete.html')

