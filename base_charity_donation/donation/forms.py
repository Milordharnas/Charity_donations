from django import forms
from donation.models import Donation, Category


class LocalisationForm(forms.Form):
    address = forms.CharField(label="address", max_length=64)
    city = forms.CharField(label="city", max_length=64)
    zip_code = forms.CharField(label="zip_code", max_length=7)
    phone_number = forms.IntegerField(label="phone_number")
    date_recive = forms.DateField(label="date_recive")
    hour_recive = forms.DateTimeField(label="hour_recive")
    comment = forms.CharField(label="comment", max_length=255)


class UserSettingsForm(forms.Form):
    firstName = forms.CharField(label="Imię", max_length=100)
    lastName = forms.CharField(label="Nazwisko", max_length=100)
    email = forms.EmailField(label="Email", max_length=100)
    password = forms.CharField(
        label="haslo", max_length=100, widget=forms.PasswordInput
    )
    new_password = forms.CharField(
        label="nowe haslo", max_length=100, widget=forms.PasswordInput
    )
