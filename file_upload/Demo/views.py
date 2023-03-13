from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import demo_form
from .models import Demo_Models

def demoView(request):
    if request.method == "POST":
        form = demo_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = demo_form()
    return render(request,"Demo/demo.html",{'form':form})
        

def show(request):
    data = Demo_Models.objects.all() or ''
    return render(request,"Demo/show.html",{'data':data})
    

def success(request):
    return HttpResponse("Successfully submited")


