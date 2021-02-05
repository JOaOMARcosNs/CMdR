from django.urls import path
from .views import Home

urlpatterns = [
    path('', Home.as_view(), name='index'),
    # path('home/', Home_home.as_view(), name='home')

]