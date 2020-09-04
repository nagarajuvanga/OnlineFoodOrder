
from django.urls import path

from pwn import views

urlpatterns = [

    path('',views.showIndex,name='pwn_main'),
    path('pwn_login_check/',views.pwn_login_check,name='pwn_login_check'),
    path('welcome/',views.welcome,name='welcome'),
    path('state/',views.openState,name='state'),
    path('city/',views.openCity,name='city'),
    path('cuisine/',views.openCusine,name='cuisine'),
    path('vendor/',views.openVendor,name='vendor'),
    path('resports/',views.openReporsts,name='reports'),
    path('logout/',views.pwn_login_check,name='logout'),
]
