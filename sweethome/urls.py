from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add', views.add, name="add"),
    path('playing/', views.playing, name="playing"),
    path('cooking/',views.cooking,name="cooking"),
    path('gardening/', views.gardening, name="gardening"),
]