from django.shortcuts import render, get_object_or_404,redirect
from django.views import View
from .models import Item
from .forms import ItemForm


class home(View):
    def get(self,request,*args,**kwargs):
        items = Item.objects.all()
        expired = Item.objects.values('is_expired')
        completed = Item.objects.values('is_completed')
        context={'items':items,'expired':expired,'completed':completed}
        return render(request,'base/home.html',context)

class itemview(View):
    def get(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        item_instance = get_object_or_404(Item,pk=pk)
        return render(request,'base/item.html',{'item':item_instance})

class create(View):
    def get(self,request,*args,**kwargs):
        form=ItemForm()
        context={'form':form}
        return render(request,'base/createupdate.html',context)
    def post(self,request,*args,**kwargs):
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')


class update(View):
    def get(self,request,*args,**kwargs):
        return render(request,'base/createupdate.html')

class delete(View):
    def get(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        item = Item.objects.get(id=pk)
        return render(request,'base/delete.html',{'obj':item})
    def post(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        item = Item.objects.get(id=pk)
        item.delete()
        return redirect('home')

