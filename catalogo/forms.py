from django import forms
from .models import Obra

class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        # Indicamos qué campos queremos que rellene el usuario
        fields = ['titulo', 'compositor', 'tipo', 'ano_composicion', 'duracion_minutos', 'num_instrumentos', 'partitura']