"""austruckie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from facedetectionapp.views import index_view, video_feed
from homeapp.views import home_view, requestAccess, passwordasking, check_list, about_us, rules
from mapapp.views import map_view



urlpatterns = [
    path('', passwordasking, name = 'start'),
    path('home', home_view, name = 'home'),
    path('face', index_view, name = 'camera'),
    path('video', video_feed, name = 'video'),
    path('admin/', admin.site.urls),
    path('checklist', check_list, name='check_list'),
    path('aboutus', about_us, name = 'aboutus'),
    path('rules', rules, name = 'rules'),
    path('access', requestAccess, name='access'),
    path('map',map_view, name='mapview')
]
