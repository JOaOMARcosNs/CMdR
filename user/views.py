from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import UserForm
from django.urls import reverse_lazy
# Create your views here.

class UserCreate(CreateView):
    template_name = "user/create-user.html"
    form_class = UserForm
    success_url = reverse_lazy('login')