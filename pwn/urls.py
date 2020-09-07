"""OnlineFood URL Configuration

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

from django.conf.urls.static import static
from django.urls import path

from OnlineFood import settings
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
    path('savestate/',views.savestate,name='savestate'),
    path('updatestate/',views.updatestate,name='updatestate'),
    path('updatestateid/',views.updatedstate,name='updatedstate'),
    path('state_delete/',views.state_delete,name='state_delete'),


    path('savecity/',views.savecity,name='savecity'),
    path('updatecity/',views.updatecity,name='updatecity'),
    path('updatedcity/',views.updatedcity,name='updatedcity'),
    path('cdelete/',views.cdelete,name='cdelete'),


    path('savecuisine/',views.savecuisine,name='savecuisine'),
    path('updatecuisine/',views.updatecuisine,name='updatecuisine'),
    path('updatecuisine/',views.updatedcuisine,name='updatedcuisine'),
    path('dcuisine/',views.delete_cuisine,name='delete_cuisine')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)