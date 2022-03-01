
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    #home
    path('', include('Menu.urls')),
    #accounts
    path('accounts/', include('django.contrib.auth.urls')),


    #Components
    #Authentication
    path('authentication_',include('Authentication.urls')),

    
   
]
