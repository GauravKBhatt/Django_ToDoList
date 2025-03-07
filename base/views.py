from django.shortcuts import render, get_object_or_404,redirect
from django.views import View
from .models import Item
from .forms import ItemForm
from django.db.models import Q


class home(View):
    def get(self, request, *args, **kwargs):
        expired = Item.objects.filter(is_expired=True)
        completed = Item.objects.filter(Q(is_expired=False) & Q(is_completed=True))
        incomplete = Item.objects.filter(Q(is_expired=False) & Q(is_completed=False))
        context = {'expired': expired, 'completed': completed, 'incomplete': incomplete}
        return render(request, 'base/home.html', context)

    def post(self, request, *args, **kwargs):
        pk = request.POST.get('name')
        items = Item.objects.filter(name__icontains=pk)

        # Re-fetch get method data
        expired = Item.objects.filter(is_expired=True)
        completed = Item.objects.filter(Q(is_expired=False) & Q(is_completed=True))
        incomplete = Item.objects.filter(Q(is_expired=False) & Q(is_completed=False))

        context = {
            'items': items,
            'expired': expired,
            'completed': completed,
            'incomplete': incomplete
        }
        return render(request, 'base/home.html', context)


class itemview(View):
    def get(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        item_instance = get_object_or_404(Item,pk=pk)
        return render(request,'base/item.html',{'item':item_instance})
    def post(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        item = Item.objects.get(id=pk)
        item.is_completed=True
        item.save()
        return redirect('home')

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

