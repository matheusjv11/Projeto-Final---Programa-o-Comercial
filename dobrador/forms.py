from django import forms
from dobrador.models import Dobrador

class FormularioDobrador(forms.ModelForm):

    class Meta:
        model = Dobrador
        exclude = []