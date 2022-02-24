from django.contrib import admin
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login, name="login"),
    #path('', views.index,name="index" ),
    path('dashboard', views.index,name="index"),
    path('calendar', views.calendar,name="calendar"),
    path('chatbot', views.chatbot,name="chatbot"),
    path('dashboard_map', views.dashboarddmap, name='dashboard_map'),
    path('calendar', views.calendar,name="calendar"),
    path('avancer', views.avancer,name="avancer"),
    path('maj_offre', views.maj_offre,name="maj_offre"),
    path('cv', views.cv, name="cv"),
    path('tradu', views.tradu,name="tradu"),
    path('lettre_motivation', views.coverletter,name="lettre_motivation"),

    
    
    


]