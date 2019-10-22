from django.views.generic import TemplateView, FormView, CreateView
from django.views import View
from donation.models import *
from donation.functions import *
from django.core.paginator import Paginator
from donation.forms import RegisterForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexPage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, page_nr=1):
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
        return ctx


class LoginPage(TemplateView):
    template_name = "login.html"


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "register.html"


# class RegisterPage(View):
#     def get(self,request):
#         form = RegisterForm()
#         return render(request,'register.html',{'form':form})
#     def post(self,request):
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['email']
#             firstName = form.cleaned_data['firstName']
#             lastName = form.cleaned_data['lastName']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             passwordAgain = form.cleaned_data['passwordAgain']
#             if User.objects.filter(username = username).exists():
#                 ctx = {
#                     'form':form ,
#                     'msg' : 'Uzytkownik istnieje'
#                 }
#                 return render(request, 'register.html', ctx)
#             User.objects.create_user(username=username, email=email, password=password,first_name = firstName, last_name = lastName)
#             return HttpResponseRedirect('/login')


class AddDonationPage(LoginRequiredMixin, TemplateView):
    template_name = "form.html"

    def get_context_data(self):
        ctx = {"categories": Category.objects.all()}
        return ctx


class UserProfilPage(LoginRequiredMixin, TemplateView):
    template_name = "profil.html"
