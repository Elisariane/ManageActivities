from django.views.generic import TemplateView

# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"


class LoginView(TemplateView):
    template_name = "accounts/login.html"


class RegisterView(TemplateView):
    template_name = "accounts/register.html"


class HomeView(TemplateView):
    template_name = "home.html"
