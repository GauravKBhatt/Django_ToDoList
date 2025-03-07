from django.shortcuts import render, get_object_or_404,redirect
from django.views import View
from .models import Item
from .forms import ItemForm
from django.db.models import Q
from django.utils.dateparse import parse_datetime
from datetime import datetime
from django.utils import timezone


class home(View):
    def get(self, request, *args, **kwargs):
        expired = Item.objects.filter(is_expired=True)
        completed = Item.objects.filter(Q(is_expired=False) & Q(is_completed=True))
        incomplete = Item.objects.filter(Q(is_expired=False) & Q(is_completed=False))
        context = {'expired': expired, 'completed': completed, 'incomplete': incomplete}
        return render(request, 'base/home.html', context)

    def post(self, request, *args, **kwargs):
        
        default_start_datetime_str = '1900-01-01T10:00'
        default_end_datetime_str = '2100-01-02T10:00'
        
        name = request.POST.get('name', '').strip()
        start_str = request.POST.get('start')
        end_str = request.POST.get('end')
        
        start = parse_datetime(start_str) if start_str else parse_datetime(default_start_datetime_str)
        end = parse_datetime(end_str) if end_str else parse_datetime(default_end_datetime_str)

            
        if start and timezone.is_naive(start):
            start = timezone.make_aware(start)
        if end and timezone.is_naive(end):
            end = timezone.make_aware(end)
            
        items = Item.objects.filter(
            Q(name__icontains=name) & Q(created__gte=start) & Q(ending__lte=end)
        )
        
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

