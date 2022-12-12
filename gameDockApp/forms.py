from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from gameDockApp.models import Pedido

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user

class PedidoForm(forms.Form):
    nombre = forms.CharField(max_length=150, required=True)
    direccion = forms.CharField(max_length=200, required=True)
    codigo_postal = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = Pedido
        fields = ("nombre", "direccion", "codigo_postal", "email")
