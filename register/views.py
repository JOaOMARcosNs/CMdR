from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Nationality, About, Homeless, Addiction, Disease

from django.urls import reverse_lazy


# Create your views here.

######################################################### CreateView #########################################################
class NationalityCreate(CreateView):
    model = Nationality
    fields = ['city', 'state']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-nationality')


class AboutCreate(CreateView):
    model = About
    fields = ['description', 'history', 'sexual_orientation', 'breed', 'ethnicity', 'school_level']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-about')

class HomelessCreate(CreateView):
    model = Homeless
    fields = ['frist_name','second_name','nickname','birth_date','gender','cpf','rg','issuing_body','height','weight','blood_type','nationality','about']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-homeless')

class AddictionCreate(CreateView):
    model = Addiction
    fields = ['name_addiction', 'type_addiction', 'homeless']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-addiction')

class DiseaseCreate(CreateView):
    model = Disease
    fields = ['name_disease', 'type_disease', 'homeless']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-disease')



######################################################### UpdateView  #########################################################

class NationalityUpdate(UpdateView):
    model = Nationality
    fields = ['city', 'state']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-nationality')

class AboutUpdate(UpdateView):
    model = About
    fields = ['description', 'history', 'sexual_orientation', 'breed', 'ethnicity', 'school_level']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-about')

class HomelessUpdate(UpdateView):
    model = Homeless
    fields = ['frist_name','second_name','nickname','birth_date','gender','cpf','rg','issuing_body','height','weight','blood_type','nationality','about']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-homeless')

class AddictionUpdate(UpdateView):
    model = Addiction
    fields = ['name_addiction', 'type_addiction', 'homeless']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-addiction')

class DiseaseUpdate(UpdateView):
    model = Disease
    fields = ['name_disease', 'type_disease', 'homeless']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-disease')


######################################################### DeleteView  #########################################################

class NationalityDelete(DeleteView):
    model = Nationality
    template_name = 'register/form-excluir.html'
    success_url = reverse_lazy('list-nationality')

class AboutDelete(DeleteView):
    model = About
    template_name = 'register/form-excluir.html'
    success_url = reverse_lazy('list-about')


class HomelessDelete(DeleteView):
    model = Homeless
    template_name = 'register/form-excluir.html'
    success_url = reverse_lazy('list-homeless')

class AddictionDelete(DeleteView):
    model = Addiction
    template_name = 'register/form-excluir.html'
    success_url = reverse_lazy('list-addiction')

class DiseaseDelete(DeleteView):
    model = Disease
    template_name = 'register/form-excluir.html'
    success_url = reverse_lazy('list-disease')


######################################################### ListeView  #########################################################

class NationalityList(ListView):
    model = Nationality
    template_name =  'register/list/natiomality.html'


class AboutList(ListView):
    model = About
    template_name = 'register/list/about.html'


class HomelessList(ListView):
    model = Homeless
    template_name = 'register/list/homeless.html'

class AddictionList(ListView):
    model = Addiction
    template_name = 'register/list/addiction.html'

class DiseaseList(ListView):
    model = Disease
    template_name = 'register/list/disease.html'

