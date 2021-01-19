from django.urls import path
from .views import Home, Home_home

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('', Home_home.as_view(), name='home-home')

]