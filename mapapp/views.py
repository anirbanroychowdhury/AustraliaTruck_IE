from django.shortcuts import render

# Create your views here.
def map_view(request, *args, **kwargs):
    return render(request,"maps.html",{})