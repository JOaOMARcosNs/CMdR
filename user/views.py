from django.views.generic.edit import CreateView

from django.contrib.auth.models import User, Group

from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

from django.contrib.auth.mixins import LoginRequiredMixin

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

class MyPasswordChangeView(PasswordChangeView):
    template_name = "user/password_change.html"
    success_url = reverse_lazy('password-chage-done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Change Password"
        context['button'] = "Change"
        

        return context


class MyPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "user/password_reset_done.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Password changed successfully"
        context['button'] = "Home"
        

        return context

