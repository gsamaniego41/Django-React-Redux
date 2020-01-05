from django.contrib import admin
from django.urls import path, include 
# include allows us to bring in a separate file

urlpatterns = [
    path('', include('frontend.urls')),
    path('', include('leads.urls')),
]
