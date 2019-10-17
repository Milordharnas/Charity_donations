from django.views.generic import TemplateView
from donation.models import *
from donation.functions import *


class IndexPage(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        ctx = {
            "all_donates": count_from_Donation().quantity,
            "quantity_institutions": count_from_Donation().institution,
            "fundations": Institution.objects.filter(types=1).order_by("name"),
            "non_governmental_organizations": Institution.objects.filter(
                types=2
            ).order_by("name"),
            "local_collection": Institution.objects.filter(types=3).order_by("name"),
        }
        return ctx


class LoginPage(TemplateView):
    template_name = "login.html"


class RegisterPage(TemplateView):
    template_name = "register.html"


class AddDonationPage(TemplateView):
    template_name = "form.html"
