from django.views.generic.edit import CreateView

from .models import Nationality, About, Homeless

from django.urls import reverse_lazy


# Create your views here.

class NationalityCreate(CreateView):
    model = Nationality
    fields = ['city', 'state']
    template_name = 'register/form.html'
    success_url = reverse_lazy('home-home')


class AboutCreate(CreateView):
    model = About
    fields = ['description', 'history', 'sexual_orientation', 'breed', 'ethnicity', 'school_level']
    template_name = 'register/form.html'
    success_url = reverse_lazy('home-home')

class HomelessCreate(CreateView):
    model = Homeless
    fields = ['frist_name','second_name','nickname','birth_date','gender','cpf','rg','issuing_body','height','weight','blood_type','nationality','about']
    template_name = 'register/form.html'
    success_url = reverse_lazy('home-home')