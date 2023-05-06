from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', asosiy),
    path('fanlar/', fanlar),
    path('fan_ochir/<int:son>/', fan_ochir),
    path('yonalishlar/', yonalishlar),
    path('yonalish_ochir/<int:son>/', yonalish_ochir),
    path('ustozlar/', ustozlar),
    path('ustoz_ochir/<int:son>/', ustoz_ochir),
]