from django.urls import path
from .views import NationalityCreate, AboutCreate, HomelessCreate
# AboutCreate

urlpatterns = [
    path('register/nationality/', NationalityCreate.as_view(), name='register-nationality'),
    path('register/about/', AboutCreate.as_view(), name='register-about'),
    path('register/homeless/', HomelessCreate.as_view(), name='register-homeless'),
]