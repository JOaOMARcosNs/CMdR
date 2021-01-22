from django.urls import path
from .views import NationalityCreate, AboutCreate, HomelessCreate, AddictionCreate, DiseaseCreate
from .views import NationalityUpdate, AboutUpdate, HomelessUpdate, AddictionUpdate, DiseaseUpdate
from .views import NationalityDelete, AboutDelete, HomelessDelete, AddictionDelete, DiseaseDelete
from .views import NationalityList, AboutList, HomelessList, AddictionList, DiseaseList
# AboutCreate

urlpatterns = [
######################################################### CreateView #########################################################
    path('register/nationality/', NationalityCreate.as_view(), name='register-nationality'),
    path('register/about/', AboutCreate.as_view(), name='register-about'),
    path('register/homeless/', HomelessCreate.as_view(), name='register-homeless'),
    path('register/addiction/', AddictionCreate.as_view(), name='register-addiction'),
    path('register/disease/', DiseaseCreate.as_view(), name='register-disease'),

######################################################### UpdateView  #########################################################
    path('edit/nationality/<int:pk>/', NationalityUpdate.as_view(), name='edit-nationality'),
    path('edit/about/<int:pk>/', AboutUpdate.as_view(), name='edit-about'),
    path('edit/homeless/<int:pk>/', HomelessUpdate.as_view(), name='edit-homeless'),
    path('edit/addiction/<int:pk>/', AddictionUpdate.as_view(), name='edit-addiction'),
    path('edit/disease/<int:pk>/', DiseaseUpdate.as_view(), name='edit-disease'),

######################################################### DeleteView  #########################################################
    path('delete/nationality/<int:pk>/', NationalityDelete.as_view(), name='delete-nationality'),
    path('delete/about/<int:pk>/', AboutDelete.as_view(), name='delete-about'),
    path('delete/homeless/<int:pk>/', HomelessDelete.as_view(), name='delete-homeless'),
    path('delete/addiction/<int:pk>/', AddictionDelete.as_view(), name='delete-addiction'),
    path('delete/disease/<int:pk>/', DiseaseDelete.as_view(), name='delete-disease'),

######################################################### ListeView  #########################################################
    path('list/nationality/', NationalityList.as_view(), name='list-nationality'),
    path('list/about/', AboutList.as_view(), name='list-about'),
    path('list/homeless/', HomelessList.as_view(), name='list-homeless'),
    path('list/addiction/', AddictionList.as_view(), name='list-addiction'),
    path('list/disease/', DiseaseList.as_view(), name='list-disease'),
]