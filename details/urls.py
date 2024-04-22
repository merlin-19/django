from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.students, name="students"),
    path('set_session/', views.set_session, name="set_session"),
    path('get_session/', views.get_session, name="get_session"),
]
