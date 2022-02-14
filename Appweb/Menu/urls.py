from django.contrib import admin
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login, name="login"),
    #path('', views.index,name="index" ),
    path('dashboard', views.index,name="index"),
    path('calendar', views.calendar,name="calendar"),
    path('chat', views.chat,name="chat"),
    path('dashboard_map', views.dashboarddmap, name='dashboard_map'),
    path('calendar', views.calendar,name="calendar"),
    path('avancer', views.avancer,name="avancer"),



]