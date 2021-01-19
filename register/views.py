from django.views.generic.edit import CreateView

from .models import Nationality, About

from django.urls import reverse_lazy


# Create your views here.

class NationalityCreate(CreateView):
    model = Nationality
    fields = ['city', 'state']
    template_name = 'register/form.html'
    success_url = reverse_lazy('home')


class AboutCreate(CreateView):
    model = About
    fields = ['description', 'history', 'sexual_orientation', 'breed', 'ethnicity', 'school_level']
    template_name = 'register/form.html'
    success_url = reverse_lazy('home')
