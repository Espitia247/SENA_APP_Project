from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    """Formulario basado en modelo para crear y editar cursos"""
    
    class Meta:
        model = Curso
        fields = [
            'codigo',
            'nombre',
            'programa',
            'instructor_coordinador',
            'fecha_inicio',
            'fecha_fin',
            'horario',
            'aula',
            'cupos_maximos',
            'estado',
            'observaciones',
        ]
        
        # Widgets para aplicar estilos de Bootstrap (clases CSS)
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 2670123'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'programa': forms.Select(attrs={'class': 'form-select'}),
            'instructor_coordinador': forms.Select(attrs={'class': 'form-select'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'horario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Lunes a Viernes 6am - 12pm'}),
            'aula': forms.TextInput(attrs={'class': 'form-control'}),
            'cupos_maximos': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def clean_cupos_maximos(self):
        """Validar que los cupos sean positivos"""
        cupos = self.cleaned_data.get('cupos_maximos')
        if cupos is not None and cupos <= 0:
            raise forms.ValidationError("El número de cupos debe ser mayor a 0.")
        return cupos

    def clean(self):
        """Validación general del formulario (Fechas)"""
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')

        # Verificar que la fecha de fin no sea anterior a la de inicio
        if fecha_inicio and fecha_fin:
            if fecha_fin < fecha_inicio:
                raise forms.ValidationError("La fecha de finalización no puede ser anterior a la fecha de inicio.")
        
        return cleaned_data