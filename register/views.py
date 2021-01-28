from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView

from .models import Nationality, About, Homeless, Addiction, Disease
from .forms import HomelessForm

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin


# Create your views here.

######################################################### CreateView #########################################################
class NationalityCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = Nationality
    fields = ['city', 'state']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-nationality')

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

class HomelessCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    form_class = HomelessForm
    model = Homeless
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-homeless')

class AddictionCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = Addiction
    fields = ['name_addiction', 'type_addiction', 'homeless']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-addiction')

class DiseaseCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = Disease
    fields = ['name_disease', 'type_disease', 'homeless']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-disease')



######################################################### UpdateView  #########################################################

class NationalityUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = Nationality
    fields = ['city', 'state']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-nationality')

class AboutUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = About
    fields = ['description', 'history', 'sexual_orientation', 'breed', 'ethnicity', 'school_level']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-about')

class HomelessUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = Homeless
    fields = ['frist_name','second_name','nickname','birth_date','gender','cpf','rg','issuing_body','height','weight','blood_type','nationality','about']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-homeless')

class AddictionUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = Addiction
    fields = ['name_addiction', 'type_addiction', 'homeless']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-addiction')

class DiseaseUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = Disease
    fields = ['name_disease', 'type_disease', 'homeless']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-disease')


######################################################### DeleteView  #########################################################

class NationalityDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"admins"
    model = Nationality
    template_name = 'register/form-excluir.html'
    success_url = reverse_lazy('list-nationality')

class AboutDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"admins"
    model = About
    template_name = 'register/form-excluir.html'
    success_url = reverse_lazy('list-about')


class HomelessDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"admins"
    model = Homeless
    template_name = 'register/form-excluir.html'
    success_url = reverse_lazy('list-homeless')

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


######################################################### ListeView  #########################################################

class NationalityList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user", u"visitor"]
    model = Nationality
    template_name =  'register/list/natiomality.html'


class AboutList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user", u"visitor"]
    model = About
    template_name = 'register/list/about.html'


class HomelessList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user", u"visitor"]
    model = Homeless
    template_name = 'register/list/homeless.html'

class AddictionList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user", u"visitor"]
    model = Addiction
    template_name = 'register/list/addiction.html'

class DiseaseList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user", u"visitor"]
    model = Disease
    template_name = 'register/list/disease.html'
