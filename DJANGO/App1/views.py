from django.shortcuts import render
from App1.form import*

# Create your views here.
def base(request):
    data=Employee.objects.all()
    return render(request,'data.html',{'data1':data})
def form1(request):
    form=Empform()
    if(request.method==('POST')):
        form=Empform(request.POST)
        if form.is_valid():
            form.save()
            return base(request)
    return render(request,'form1.html',{'form':form})

def form2(request):
    if request.method=='POST':
        form=Empform(request.POST)
        if form.is_valid():
            form.save()
            return base(request)  
    return render(request,'form2.html')

def form3(request):
    if request.method=='POST':
        n=request.POST['n']
        m=request.POST['m']
        o=request.POST['o']
        q=request.POST['q']
        s=Employee.objects.create(emp_id=n,emp_name=m,emp_designation=o,emp_salary=q)
        s.save()
        return base(request)
    return render(request,'form3.html')