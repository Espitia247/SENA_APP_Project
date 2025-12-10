from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from .models import Instructor
from django.shortcuts import get_object_or_404

from instructores.forms import InstructorForm
from django.views import generic
from django.contrib import messages
from django.views.generic import FormView

# Create your views here.

def instructores(request):
    lista_instructores = Instructor.objects.all()
    template = loader.get_template('lista_instructores.html')
    
    context = {
        'lista_instructores': lista_instructores,
        'total_instructores': lista_instructores.count(),
    }
    return HttpResponse(template.render(context, request))

def detalle_instructor(request, id_instructor):
  instructor = Instructor.objects.get(id=id_instructor)
  template = loader.get_template('detalle_instructor.html')
  context = {
    'instructor': instructor,
  }
  return HttpResponse(template.render(context, request))

class InstructorCreateView(generic.CreateView):
    """Vista para crear un nuevo instructor"""
    model = Instructor
    form_class = InstructorForm
    template_name = 'crear_instructor.html'
    success_url = reverse_lazy('instructores:lista_instructores')
    
    def form_valid(self, form):
        messages.success(
            self.request,
            f'El instructor {form.instance.nombre_completo()} ha sido registrado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)


class InstructorUpdateView(generic.UpdateView):
    """Vista para actualizar un instructor existente"""
    model = Instructor
    form_class = InstructorForm
    template_name = 'editar_instructor.html'
    success_url = reverse_lazy('instructores:lista_instructores')
    pk_url_kwarg = 'instructor_id'
    
    def form_valid(self, form):
        messages.success(
            self.request,
            f'El instructor {form.instance.nombre_completo()} ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)


class InstructorDeleteView(generic.DeleteView):
    """Vista para eliminar un instructor"""
    model = Instructor
    template_name = 'eliminar_instructor.html'
    success_url = reverse_lazy('instructores:lista_instructores')
    pk_url_kwarg = 'instructor_id'
    
    def delete(self, request, *args, **kwargs):
        instructor = self.get_object()
        messages.success(
            request,
            f'El instructor {instructor.nombre_completo()} ha sido eliminado exitosamente.'
        )
        return super().delete(request, *args, **kwargs)