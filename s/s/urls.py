from django.contrib import admin
from django.urls import path
from preal import views


urlpatterns = [
    path('',views.info,kwargs = {'name':'Семён', 'age':'16' }),
    path('about',views.about,kwargs = {'From':'Серов', 'oc':'Пойдёт','s':'Да'}),
    path('contact',views.contact, kwargs = {'Tg': "@SemGusb",'tel':'8-996-170-37-79','Github':'https://github.com/SemGusb'}),
]
