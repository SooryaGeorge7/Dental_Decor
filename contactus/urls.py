from . import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
     path('', views.contact_us, name='contact_us'),
]
