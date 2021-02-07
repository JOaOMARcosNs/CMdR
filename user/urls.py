from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
            template_name='user/login.html'
        ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registerUser/', UserCreate.as_view(), name='register-user'),
    path('chage-password/', MyPasswordChangeView.as_view(), name='password-chage'),
    path('chage-password/done/', MyPasswordChangeDoneView.as_view(), name='password-chage-done'),
    path('edit-profile/', UserEditView.as_view(), name='edit-profile'),
    
    
]