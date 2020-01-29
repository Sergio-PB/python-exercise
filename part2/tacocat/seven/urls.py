"""seven URL Configuration"""

from django.urls import path, include

from .views import get_form

urlpatterns = [
    path('', get_form, name='form'),
]
