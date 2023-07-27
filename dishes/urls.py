from django.contrib import admin
from django.urls import path
from dishes import views
# from .views import csv_data

urlpatterns = [
    # path('', views.index),
    path('', views.dishes, name="dishes"),
]