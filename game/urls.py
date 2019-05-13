from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('role/',  views.role, name="role"),
    path('choose_area/', views.choose_area, name="choose_area"),
    path('choose_process/',views.choose_process,name="choose_process"),
    path('area_people/', views.area_people, name="area_people"),
        path('situation_create/', views.situation_create, name="situation_create"),
    path('result/<int:round_num>', views.result, name="result"),
    path('endgame/', views.endgame, name="endgame"),
    path('signup/',  views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout,name="logout"),
]
