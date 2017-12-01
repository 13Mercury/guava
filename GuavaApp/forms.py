from django import forms
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Area_Verde, Foto, Aportacion, Peticion, Adopcion
from django.core.validators import RegexValidator

class Users_Form(UserCreationForm):
    nombre = forms.CharField(max_length=100, validators=[
        RegexValidator(
            regex='^[a-zA-Z ]*$',
            message='Nombre solo puede contener letras',
            code='invalid_name'
        )
    ])
    telefono = forms.CharField(max_length=20, validators=[
        RegexValidator(
            regex='(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})',
            message='Formato de telefono erroneo.\n (123) 456 7899\n(123).456.7899\n(123)-456-7899\n123-456-7899\n123 456 7899\n1234567899',
            code='invalid_phone'
        )
    ])
    email = forms.EmailField()

class InfoForm(forms.ModelForm):
    telefono = forms.CharField(max_length=20, validators=[
        RegexValidator(
            regex='(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})',
            message='Formato de telefono erroneo.\n (123) 456 7899\n(123).456.7899\n(123)-456-7899\n123-456-7899\n123 456 7899\n1234567899',
            code='invalid_phone'
        )
    ])

    pagina = forms.CharField(max_length=20, validators=[
        RegexValidator(
            regex='(http\:\/\/|https\:\/\/)?([a-z0-9][a-z0-9\-]*\.)+[a-z0-9][a-z0-9\-]*',
            message='Pagina invalida',
            code='invalid_page'
        )
    ])
    class Meta:
        model = Usuario
        fields = ["descripcion","direccion","telefono","pagina","email"]

class AreaForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50, validators=[
        RegexValidator(
            regex='^[a-zA-Z ]*$',
            message='Nombre solo puede contener letras',
            code='invalid_name'
        )
    ])
    class Meta:
        model = Area_Verde
        fields = ["nombre","ubicacion","direccion"]

class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ["image","areaPertenece","subidaPor"]

class PeticionForm(forms.ModelForm):
    class Meta:
        model = Peticion
        fields = ["peticion","comentario"]

class AportacionForm(forms.ModelForm):
    class Meta:
        model = Aportacion
        fields = ["aportacion","comentario"]

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["image"]
