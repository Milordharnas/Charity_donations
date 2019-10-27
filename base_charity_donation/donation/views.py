from django.views.generic import TemplateView, FormView, CreateView
from django.views import View
from donation.models import *
from donation.functions import *
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate
from donation.forms import LocalisationForm, UserSettingsForm


class IndexPage(View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        page_nr = request.GET.get("page")
        if not page_nr:
            page_nr = 1
        fundations = Paginator(Institution.objects.filter(types=1).order_by("name"), 5)
        non_governmental_organizations = Paginator(
            Institution.objects.filter(types=2).order_by("name"), 5
        )
        local_collection = Paginator(
            Institution.objects.filter(types=3).order_by("name"), 5
        )
        ctx = {
            "all_donates": count_from_Donation().quantity,
            "quantity_institutions": count_from_Donation().institution,
            "fundations": fundations.get_page(page_nr),
            "non_governmental_organizations": non_governmental_organizations.get_page(
                page_nr
            ),
            "local_collection": local_collection.get_page(page_nr),
            "page_nr": page_nr,
        }
        return render(request, "index.html", ctx)


class LoginPage(TemplateView):
    template_name = "login.html"


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "register.html"


class AddDonationPage1(LoginRequiredMixin, View):
    def get(self, request):
        ctx = {"categories": Category.objects.all()}
        return render(request, "form1.html", ctx)

    def post(self, request):
        request.session["list_of_categories"] = request.POST.getlist("categories")
        print(request.POST.getlist("categories"))
        return HttpResponseRedirect("2")


class AddDonationPage2(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "form2.html")

    def post(self, request):
        request.session["quantity_bags"] = request.POST.get("bags")
        return HttpResponseRedirect("3")


class AddDonationPage3(LoginRequiredMixin, View):
    def get(self, request):
        # listCategory = ['ubrania','zabawki','ksiazki','gry','inne']
        list_of_categories = request.session.get("list_of_categories")
        instiution_list = []
        for i in range(0, len(list_of_categories)):
            instiution_list += Institution.objects.filter(
                category=Category.objects.get(name=list_of_categories[i])
            )
        ctx = {"instiution_list": instiution_list}
        return render(request, "form3.html", ctx)

    def post(self, request):
        request.session["choosen_institution"] = request.POST.get("old")
        return HttpResponseRedirect("4")


class AddDonationPage4(LoginRequiredMixin, View):
    def get(self, request):
        form = LocalisationForm()
        return render(request, "form4.html", {"form": form})

    def post(self, request):
        form = LocalisationForm(request.POST)
        if form.is_valid():
            request.session["address"] = form.cleaned_data["address"]
            request.session["city"] = form.cleaned_data["city"]
            request.session["zip_code"] = form.cleaned_data["zip_code"]
            request.session["phone_number"] = form.cleaned_data["phone_number"]
            request.session["date_recive"] = form.cleaned_data["date_recive"]
            request.session["hour_recive"] = form.cleaned_data["hour_recive"]
            request.session["comment"] = form.cleaned_data["comment"]
            return HttpResponseRedirect("5")
        return HttpResponseRedirect("4")


class AddDonationPage5(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "form5.html")

    def post(self, request):
        pass


class UserProfilPage(LoginRequiredMixin, TemplateView):
    template_name = "profil.html"


class UserSettingsPage(LoginRequiredMixin, View):
    def get(self, request, user_id):
        form = UserSettingsForm()
        return render(request, "settings.html", {"form": form})

    def post(self, request, user_id):
        form = UserSettingsForm(request.POST)
        user = request.user
        print(user)
        if form.is_valid():
            password = form.cleaned_data["password"]
            password_correct = authenticate(username=user.username, password=password)
            if password_correct:
                user.first_name = form.cleaned_data["firstName"]
                user.last_name = form.cleaned_data["lastName"]
                user.email = form.cleaned_data["email"]
                user.password = form.cleaned_data["password"]
                user.save()
        return HttpResponseRedirect(
            "http://127.0.0.1:8000/ustawienia/{}".format(user_id)
        )
