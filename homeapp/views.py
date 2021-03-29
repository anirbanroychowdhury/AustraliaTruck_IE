from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request,"home.html",{})

def check_list(request, *args, **kwargs):
    return render(request,"checklist.html",{})

def about_us(request, *args, **kwargs):
    return render(request,"aboutus.html",{})