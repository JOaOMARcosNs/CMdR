from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Nationality, About, Homeless, Addiction, Disease

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

######################################################### CreateView #########################################################
class NationalityCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Nationality
    fields = ['city', 'state']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-nationality')


class AboutCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = About
    fields = ['description', 'history', 'sexual_orientation', 'breed', 'ethnicity', 'school_level']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-about')

class HomelessCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Homeless
    fields = ['frist_name','second_name','nickname','birth_date','gender','cpf','rg','issuing_body','height','weight','blood_type','nationality','about']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-homeless')

class AddictionCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Addiction
    fields = ['name_addiction', 'type_addiction', 'homeless']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-addiction')

class DiseaseCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Disease
    fields = ['name_disease', 'type_disease', 'homeless']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-disease')



######################################################### UpdateView  #########################################################

class NationalityUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Nationality
    fields = ['city', 'state']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-nationality')

class AboutUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = About
    fields = ['description', 'history', 'sexual_orientation', 'breed', 'ethnicity', 'school_level']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-about')

class HomelessUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Homeless
    fields = ['frist_name','second_name','nickname','birth_date','gender','cpf','rg','issuing_body','height','weight','blood_type','nationality','about']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-homeless')

class AddictionUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Addiction
    fields = ['name_addiction', 'type_addiction', 'homeless']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-addiction')

class DiseaseUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Disease
    fields = ['name_disease', 'type_disease', 'homeless']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-disease')


######################################################### DeleteView  #########################################################

class NationalityDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Nationality
    template_name = 'register/form-excluir.html'
    success_url = reverse_lazy('list-nationality')

class AboutDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = About
    template_name = 'register/form-excluir.html'
    success_url = reverse_lazy('list-about')


class HomelessDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Homeless
    template_name = 'register/form-excluir.html'
    success_url = reverse_lazy('list-homeless')

class AddictionDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Addiction
    template_name = 'register/form-excluir.html'
    success_url = reverse_lazy('list-addiction')

class DiseaseDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Disease
    template_name = 'register/form-excluir.html'
    success_url = reverse_lazy('list-disease')


######################################################### ListeView  #########################################################

class NationalityList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Nationality
    template_name =  'register/list/natiomality.html'


class AboutList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = About
    template_name = 'register/list/about.html'


class HomelessList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Homeless
    template_name = 'register/list/homeless.html'

class AddictionList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Addiction
    template_name = 'register/list/addiction.html'

class DiseaseList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Disease
    template_name = 'register/list/disease.html'
