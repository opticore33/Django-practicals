from django.http import HttpResponse
from django.shortcuts import render
from .forms import userInformation
from userinfo.models import user


def userdata(request):
    data = {'fn':userInformation()}
    if request.method == "POST":
        form = userInformation(request.POST)
        print(request.POST)
        if form.is_valid():
            print(type(form),"hi")
            form.save()
        
        

    return render(request,"form.html",data)

def show(request):
    user_data = user.objects.all().order_by('name') # -name for descending order by name
    
    user_d = {
        "user_data": user_data
    }

    return render(request,"show.html",user_d)

def Search(request):
    user_data = {}
    if request.method == "GET":
        print(request.GET)
        all_user = user.objects.all()
        key = request.GET.get('search')
        print(key)
        userr = user.objects.filter(name = key)
        
        # print(userr)
        # print(all_user)
        try:
            if userr[0] in all_user:
                user_data = {'user_info':userr}
                print('hi',user_data)
                return render(request,"Search.html",user_data)
        except IndexError:
            data = {
                'error': "user not found"
            }
            return render(request,"Search.html",data)
            
            
    