from django.urls import path

from . import views
from donation.views import (
    IndexPage,
    LoginPage,
    AddDonationPage1,
    AddDonationPage2,
    AddDonationPage3,
    AddDonationPage4,
    AddDonationPage5,
    UserProfilPage,
    UserSettingsPage,
)

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("form/1", AddDonationPage1.as_view()),
    path("form/2", AddDonationPage2.as_view()),
    path("form/3", AddDonationPage3.as_view()),
    path("form/4", AddDonationPage4.as_view()),
    path("form/5", AddDonationPage5.as_view()),
    path("profil/<str:user_name>", UserProfilPage.as_view()),
    path("ustawienia/<str:user_id>", UserSettingsPage.as_view()),
]
