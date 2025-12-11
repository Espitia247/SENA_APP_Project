from django import forms
from .models import Programa

class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = '__all__' 
        
     
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'nivel_formacion': forms.Select(attrs={'class': 'form-select'}),
            'modalidad': forms.Select(attrs={'class': 'form-select'}),
            'duracion_meses': forms.NumberInput(attrs={'class': 'form-control'}),
            'duracion_horas': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'competencias': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'perfil_egreso': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'requisitos_ingreso': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'centro_formacion': forms.TextInput(attrs={'class': 'form-control'}),
            'regional': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'fecha_creacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }