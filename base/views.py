from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class home(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse("This is the home page.")

class item(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse("This is the item page.")

class create(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse("This is the create page.")

class update(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse("This is the update page.")

class delete(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse("This is the delete page.")

