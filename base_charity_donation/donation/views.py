from django.views.generic import TemplateView


class IndexPage(TemplateView):
    template_name = "index.html"


class LoginPage(TemplateView):
    template_name = "login.html"


class RegisterPage(TemplateView):
    template_name = "register.html"


class AddDonationPage(TemplateView):
    template_name = "form.html"
