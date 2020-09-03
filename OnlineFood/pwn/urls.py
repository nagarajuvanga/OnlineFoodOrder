
from django.urls import path

from pwn import views

urlpatterns = [

    path('',views.showIndex,name='pwn_main'),
    path('pwn_login_check/',views.pwn_login_check,name='pwn_login_check'),
    path('welcome/',views.welcome,name='welcome'),
]
