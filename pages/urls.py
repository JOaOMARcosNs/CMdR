from django.urls import path
from .views import Home, Home_home

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('home/', Home_home.as_view(), name='home')

]