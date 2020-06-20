from django.shortcuts import render
from rest_framework import generics
from .serializers import UserinfoSerializer, ActivityPeriodSerializer
from .models import Userinfo, ActivityPeriod
from rest_framework import viewsets
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class ListUserView(generics.ListCreateAPIView):
    queryset = Userinfo.objects.all()
    serializer_class = UserinfoSerializer


class DetailUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Userinfo.objects.all()
    serializer_class = UserinfoSerializer
