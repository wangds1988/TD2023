from django.urls import path
from django.contrib import admin

from Kapi.views import index

urlpatterns = [
    path('in/', index),
]