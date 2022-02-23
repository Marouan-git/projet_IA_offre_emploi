from django.contrib import admin
from django.urls import path,include
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    # Authentication
    path('lockscreen', views.lockscreen, name="lockscreen"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('recoverpassword', views.recoverpassword, name="recoverpassword"),
    path('login',auth_views.LoginView.as_view(template_name="Pages/Authentication/login.html") ,name='login'),
    path('logout',views.logout,name='logout'),
    path('password_change', auth_views.PasswordChangeView.as_view(template_name ='Authentication/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name ='Authentication/password_change_done.html'), name='password_change_done'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='Authentication/password_confirm.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='Authentication/password_reset.html'),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='Authentication/reset_complete.html'),name='password_reset_complete'),
 
]
