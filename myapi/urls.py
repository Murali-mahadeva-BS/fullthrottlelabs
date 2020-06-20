from django.urls import path, include
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'myapi', views.UserViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    # path('myapi/', include('rest_framework.urls', namespace='rest_framework'))
    path('', views.HomePageView.as_view(), name='home'),
    path('api/', views.ListUserView.as_view(), name='apiview'),
    path('api/<int:pk>/', views.DetailUserView.as_view(), name='apidetaiview'),
]
