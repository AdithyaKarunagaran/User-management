"""
URL configuration for vendor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from user_details import views as usapp
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Register', usapp.register, name='Register'),
    path('Address', usapp.address, name='Address'),
    path('Contact', usapp.contact, name='Contact'),
    path('VendorDetails', usapp.vendor_models, name='VendorDetails'),
    path('GetRegister',usapp.get_register, name='GetRegister'),
    path('GetAddress',usapp.get_address, name='GetAddress'),
    path('GetContact',usapp.get_contact, name='GetContact'),
    path('GetVendor', usapp.get_vendor, name = "Vendor"),
    path('RegGet/<pk>', usapp.reg_get, name = "RegGet"),
    path('AddGet/<pk>', usapp.add_get, name="ADGet"),
    path('ConGet/<pk>', usapp.con_get, name="ConGet"),
    path('VendGet/<pk>', usapp.vend_get, name="VrGet"),
    path('index', usapp.index_form, name="index"),
    path('RegSearch', usapp.reg_search, name="RegSearch"),
    path('AddSearch', usapp.add_search, name="RegSearch"),
    path('ConSearch', usapp.con_search, name="RegSearch"),
    path('VendSearch', usapp.vend_search, name="RegSearch"),
    path('DeleteReg/<pk>', usapp.delete_reg, name='DeleteReg'),
    path('DeleteAdd/<pk>', usapp.delete_add, name='DeleteAdd'),
    path('DeleteCon/<pk>', usapp.delete_con, name='DeleteCon'),
    path('DeleteVend/<pk>', usapp.delete_vend, name='DeleteVend'),
    path('Login', usapp.login, name='Login')
]


