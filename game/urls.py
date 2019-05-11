from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('role/',  views.role, name="role"),
    path('choose_area/', views.choose_area, name="choose_area"),
    path('area_people/', views.area_people, name="area_people"),
    path('result/', views.result, name="result"),

]
