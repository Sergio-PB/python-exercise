"""tacocat URL Configuration"""
from django.urls import path, include

urlpatterns = [
    path('seven/', include('seven.urls')),
]
