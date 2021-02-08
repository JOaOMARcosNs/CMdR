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

    path('reset-password/', auth_views.PasswordResetView.as_view(
        template_name='user/passord-reset.html'
    ), name='reset_password'),

    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(
        template_name= 'user/password-reset-sent.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name= 'user/password-reset-confirm.html'
    ), name='password_reset_confirm'),

    path('reset-password-complete/', auth_views.PasswordResetView.as_view(
        template_name= 'user/password-reset-done.html'
    ), name='password_reset_complete'),


    
    
    
]