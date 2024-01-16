from django.urls import path
from . import views

urlpatterns = [
    # Path de Service


    path('', views.services, name="services"),


  ]