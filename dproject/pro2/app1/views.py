from django.shortcuts import render
from app1.models import *
from app1.forms import *

# Create your views here.
def base(request):
    return render(request,'base.html')

def add_item(request):
    s=Empform()
    if request.method=='POST':
        s=Empform(request.POST)
        if s.is_valid():
            s.save()
            return view_item(request)
    return render(request,'add.html',{'form':s})

def view_item(request):
    d=Emp.objects.all()
    context={'data':d}
    return render(request,'view.html',context)


def edit(request,p):
    b=Emp.objects.get(pk=p)
    s=Empform(instance=b)
    if request.method=='POST':
        s=Empform(request.POST,instance=b)
        if s.is_valid():
            s.save()
            return view_item(request)
    return render(request,'edit.html',{'form':s})

def delete_item(request,p):
     b=Emp.objects.get(pk=p)
     b.delete()
     return view_item(request)

