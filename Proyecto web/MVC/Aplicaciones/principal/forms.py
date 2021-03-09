from django import forms
from .models import Persona,TipoDocumento,Ciudad


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
