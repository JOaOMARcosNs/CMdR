from django.views.generic import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name = "pages/index.html"


class Home_home(TemplateView):
    template_name = "pages/home-home.html"