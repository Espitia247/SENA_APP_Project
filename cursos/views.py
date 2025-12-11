from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views import generic
from django.contrib import messages

# Importamos el modelo y el formulario de cursos
from .models import Curso
from .forms import CursoForm

# --- Vistas Basadas en Funciones ---

def cursos(request):
    """Vista para listar todos los cursos"""
    lista_cursos = Curso.objects.all().order_by('-fecha_inicio') # Ordenados por fecha
    template = loader.get_template('lista_cursos.html')

    context = {
        'lista_cursos': lista_cursos,
        'total_cursos': lista_cursos.count(), # Agregado para el badge del HTML
    }
    return HttpResponse(template.render(context, request))

def detalle_curso(request, curso_id):
    """Vista para ver detalles de un curso específico"""
    # Usamos get_object_or_404 para manejar el error si el ID no existe
    curso = get_object_or_404(Curso, pk=curso_id)
    template = loader.get_template('detalle_curso.html') # Asegúrate de tener este HTML (opcional)
    
    context = {
        'curso': curso,
    }
    return HttpResponse(template.render(context, request))

# --- Vistas Basadas en Clases (CBV) ---

class CursoCreateView(generic.CreateView):
    """Vista para crear un nuevo curso"""
    model = Curso
    form_class = CursoForm
    template_name = 'crear_curso.html'
    success_url = reverse_lazy('cursos:lista_cursos')
    
    def form_valid(self, form):
        messages.success(
            self.request,
            f'El curso "{form.instance.nombre}" (Código: {form.instance.codigo}) ha sido registrado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)


class CursoUpdateView(generic.UpdateView):
    """Vista para actualizar un curso existente"""
    model = Curso
    form_class = CursoForm
    template_name = 'editar_curso.html'
    success_url = reverse_lazy('cursos:lista_cursos')
    pk_url_kwarg = 'curso_id' # Importante: debe coincidir con tu urls.py
    
    def form_valid(self, form):
        messages.success(
            self.request,
            f'El curso "{form.instance.nombre}" ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)


class CursoDeleteView(generic.DeleteView):
    """Vista para eliminar un curso"""
    model = Curso
    template_name = 'eliminar_curso.html'
    success_url = reverse_lazy('cursos:lista_cursos')
    pk_url_kwarg = 'curso_id' # Importante: debe coincidir con tu urls.py
    
    def delete(self, request, *args, **kwargs):
        curso = self.get_object()
        nombre_curso = curso.nombre # Guardamos el nombre antes de borrarlo para el mensaje
        messages.success(
            request,
            f'El curso "{nombre_curso}" ha sido eliminado exitosamente.'
        )
        return super().delete(request, *args, **kwargs)