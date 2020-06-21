# FullThrottleLabs Internship Project
### visit site [Here](fullthrottlelabs-internship.herokuapp.com)

## Implementation:

### Used packages:

- Django==3.0.7
- django-on-heroku==1.0.1
- djangorestframework==3.11.0
- gunicorn==20.0.4
- psycopg2-binary==2.8.5

### models.py

**ActivityPeriod** model is linked to **Userinfo** model by ForeignKey 

```python
from django.db import models


class Userinfo(models.Model):
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=100)


class ActivityPeriod(models.Model):
    activity_periods = models.ForeignKey(
        Userinfo, related_name="activity_periods", on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

```

### serializers.py

Relational serializers of Django REST framework are used and are defined in serializers.py file 

```python
from rest_framework import serializers

from .models import Userinfo, ActivityPeriod


class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ['start_time', 'end_time']


class UserinfoSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(many=True, read_only=True)

    class Meta:
        model = Userinfo
        fields = ('id', 'real_name', 'tz', 'activity_periods')

```

### views.py

models and serializers are imported and rendered using django REST framework APIview 

```python
from django.shortcuts import render
from rest_framework import generics
from .serializers import UserinfoSerializer, ActivityPeriodSerializer
from .models import Userinfo, ActivityPeriod
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class ListUserView(generics.ListCreateAPIView):
    queryset = Userinfo.objects.all()
    serializer_class = UserinfoSerializer


class DetailUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Userinfo.objects.all()
    serializer_class = UserinfoSerializer

```

### urls.py

**api/** routing displays user activity data in jason format\
**api/<<int:pk>>/** routing displays individual user activity data 

```python
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('api/', views.ListUserView.as_view(), name='apiview'),
    path('api/<int:pk>/', views.DetailUserView.as_view(), name='apidetaiview'),
]

```
