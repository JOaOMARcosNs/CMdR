from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from .forms import UserForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
# Create your views here.

class UserCreate(CreateView):
    template_name = "user/create-user.html"
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):

        group = get_object_or_404(Group, name="user")

        url = super().form_valid(form)

        self.object.groups.add(group)
        self.object.save()

        return url