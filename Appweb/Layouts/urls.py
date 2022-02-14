from django.contrib import admin
from django.urls import path
from  .import views 

urlpatterns = [
    #Vertical
    path('layoutboxed', views.layoutboxed ,name="layoutboxed"),
    path('darksidebar', views.darksidebar ,name="darksidebar"),
    path('compactsidebar', views.compactsidebar ,name="compactsidebar"),
    path('iconsidebar', views.iconsidebar ,name="iconsidebar"),
    path('preloader', views.preloader ,name="preloader"),
    path('colorsidebar', views.colorsidebar ,name="colorsidebar"),
    #Horizontal
    path('horizontal', views.horizontal ,name="horizontal"),
    path('horitopdark', views.horitopdark ,name="horitopdark"),
    path('horibox', views.horibox ,name="horibox"),
    path('horipreloader', views.horipreloader,name="horipreloader"),

]