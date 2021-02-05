from django.views.generic import TemplateView

from django.urls import reverse_lazy


from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Home(TemplateView):
    template_name = "pages/index.html"


# class Home_home(LoginRequiredMixin,TemplateView):
#     login_url = reverse_lazy('login')
#     template_name = "pages/home-home.html"