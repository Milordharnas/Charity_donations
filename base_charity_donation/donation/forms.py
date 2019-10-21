from django import forms


class RegisterForm(forms.Form):
    firstName = forms.CharField(label="Imię", max_length=100)
    lastName = forms.CharField(label="Nazwisko", max_length=100)
    email = forms.EmailField(label="Email", max_length=100)
    password = forms.CharField(
        label="Hasło", max_length=100, widget=forms.PasswordInput
    )
    passwordAgain = forms.CharField(
        label="Powtórz hasło", max_length=100, widget=forms.PasswordInput
    )
