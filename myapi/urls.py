from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('api/', views.ListUserView.as_view(), name='apiview'),
    path('api/<int:pk>/', views.DetailUserView.as_view(), name='apidetaiview'),
]
