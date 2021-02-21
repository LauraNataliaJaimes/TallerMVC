from django import forms
from .models import Persona, Ciudad, TipoDocumento

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = "__all__"


class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = "__all__"


class TipoDocumentoForm(forms.ModelForm):
    class Meta:
        model = TipoDocumento
        fields = "__all__"