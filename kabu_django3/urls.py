"""kabu_django3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from stocks import views

# app_name = 'stocks'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('get_TSE/', views.get_TSE, name="get_TSE"),
    path('get_tse_brands/', views.reg_TSE, name="reg_TSE"),
    path('get_stooq/', views.get_stooq, name="get_stooq"),
    path('reg_TSE_from_stooq/', views.reg_TSE_from_stooq, name="reg_TSE_from_stooq"),
    path('company/', views.company, name="company"),
    path('discripter/', views.boot_descripter, name="descripter"),
]
