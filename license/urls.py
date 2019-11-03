from django.urls import path
from . import views
from django.conf.urls import include,url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns =   [

    path('index/',views.index,name='index'),
    path('Signup/',views.Signup,name='Signup'),
    path('Otp/',views.Otp,name='Otp'),
    path('Retrive/',views.Retrive,name='Retrive'),
    ]

urlpatterns += staticfiles_urlpatterns()