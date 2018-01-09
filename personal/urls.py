from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('solpod_about/', views.solpod_about, name='solpod_about'),
    path('solpod_desc/', views.solpod_desc, name='solpod_desc'),
    path('solpod_result/', views.solpod_result, name='solpod_result'),
    path('lct_about/', views.lct_about, name='lct_about'),
    path('lct_pid/', views.lct_pid, name='lct_pid'),
    path('lct_result/', views.lct_result, name='lct_result'),
]
