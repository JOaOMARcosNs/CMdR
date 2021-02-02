from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView

from .models import Nationality, About, Homeless, Addiction, Disease
from .forms import HomelessForm

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from django.shortcuts import get_list_or_404

# Create your views here.

######################################################### CreateView #########################################################
class NationalityCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = Nationality
    fields = ['city', 'state']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-nationality')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Nationality registration"
        context['button'] = "Register"
        

        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        valid = super().form_valid(form)
        return valid   
 


class AboutCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = About
    fields = ['description', 'history', 'sexual_orientation', 'breed', 'ethnicity', 'school_level']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-about')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "About registration"
        context['button'] = "Register"
        

        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        valid = super().form_valid(form)
        return valid 

class HomelessCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    form_class = HomelessForm
    model = Homeless
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-homeless')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Homeless registration"
        context['button'] = "Register"
        

        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        valid = super().form_valid(form)
        return valid     
class AddictionCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = Addiction
    fields = ['name_addiction', 'type_addiction', 'homeless']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-addiction')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Addiction registration"
        context['button'] = "Register"
        

        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        valid = super().form_valid(form)
        return valid  

class DiseaseCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = Disease
    fields = ['name_disease', 'type_disease', 'homeless']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-disease')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Disease registration"
        context['button'] = "Register"
        

        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        valid = super().form_valid(form)
        return valid 

######################################################### UpdateView  #########################################################

class NationalityUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = Nationality
    fields = ['city', 'state']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-nationality')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Edit nationality records"
        context['button'] = "Save"

        return context


class AboutUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = About
    fields = ['description', 'history', 'sexual_orientation', 'breed', 'ethnicity', 'school_level']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-about')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Edit about records"
        context['button'] = "Save"

        return context

class HomelessUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = Homeless
    fields = ['frist_name','second_name','nickname','birth_date','gender','cpf','rg','issuing_body','height','weight','blood_type','nationality','about']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-homeless')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Edit homeless records"
        context['button'] = "Save"

        return context

class AddictionUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = Addiction
    fields = ['name_addiction', 'type_addiction', 'homeless']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-addiction')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Edit addiction records"
        context['button'] = "Save"

        return context

class DiseaseUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = Disease
    fields = ['name_disease', 'type_disease', 'homeless']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-disease')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Edit disease records"
        context['button'] = "Save"

        return context


######################################################### DeleteView  #########################################################

class NationalityDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"admins"
    model = Nationality
    template_name = 'register/form-excluir.html'
    success_url = reverse_lazy('list-nationality')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Delete nationality records"

        return context

    

class AboutDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"admins"
    model = About
    template_name = 'register/form-excluir.html'
    success_url = reverse_lazy('list-about')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Delete about records"

        return context


class HomelessDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"admins"
    model = Homeless
    template_name = 'register/form-excluir.html'
    success_url = reverse_lazy('list-homeless')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Delete homeless records"

        return context

class AddictionDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"admins"
    model = Addiction
    template_name = 'register/form-excluir.html'
    success_url = reverse_lazy('list-addiction')

class DiseaseDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"admins"
    model = Disease
    template_name = 'register/form-excluir.html'
    success_url = reverse_lazy('list-disease')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Delete disease records"

        return context


######################################################### ListeView  #########################################################

class NationalityList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = Nationality
    template_name =  'register/list/natiomality.html'


class AboutList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = About
    template_name = 'register/list/about.html'


class HomelessList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = Homeless
    template_name = 'register/list/homeless.html'

class AddictionList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = Addiction
    template_name = 'register/list/addiction.html'

class DiseaseList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = Disease
    template_name = 'register/list/disease.html'
