from django.urls import path

from . import views
from donation.views import IndexPage, LoginPage, AddDonationPage

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("page/<int:page_nr>/", IndexPage.as_view()),
    path("form/", AddDonationPage.as_view()),
]
