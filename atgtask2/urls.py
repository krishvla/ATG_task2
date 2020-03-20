"""atgtask2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from task2app.views import home, reg, login, check, dashboard, logout,create,search
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', home, name="home"),
    url(r'^login/', login, name="login"),
    url(r'^reg/',reg,name="reg"),
    url(r'^check/', check, name="check"),
    url(r'^dashboard/',dashboard,name="dashboard"),
    url(r'^logout/',logout,name="logout"),
    url(r'^create/',create,name="create"),
    url(r'^search/',search,name="search"),
]
