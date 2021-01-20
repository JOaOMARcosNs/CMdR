from django.urls import path
from .views import NationalityCreate, AboutCreate, HomelessCreate
from .views import NationalityUpdate, AboutUpdate, HomelessUpdate
from .views import NationalityDelete, AboutDelete, HomelessDelete
# AboutCreate

urlpatterns = [
######################################################### CreateView #########################################################
    path('register/nationality/', NationalityCreate.as_view(), name='register-nationality'),
    path('register/about/', AboutCreate.as_view(), name='register-about'),
    path('register/homeless/', HomelessCreate.as_view(), name='register-homeless'),

######################################################### UpdateView  #########################################################
    path('edit/nationality/<int:pk>/', NationalityUpdate.as_view(), name='edit-nationality'),
    path('edit/about/<int:pk>/', AboutUpdate.as_view(), name='edit-about'),
    path('edit/homeless/<int:pk>/', HomelessUpdate.as_view(), name='edit-homeless'),

######################################################### Delete  #########################################################
    path('delete/nationality/<int:pk>/', NationalityDelete.as_view(), name='delete-nationality'),
    path('delete/about/<int:pk>/', AboutDelete.as_view(), name='delete-about'),
    path('delete/homeless/<int:pk>/', HomelessDelete.as_view(), name='delete-homeless'),

]