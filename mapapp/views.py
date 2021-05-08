from django.shortcuts import render

# Create your views here.
# Open the home page. This is called after the password check
def map_view(request, *args, **kwargs):
    return render(request, "map.html",{})