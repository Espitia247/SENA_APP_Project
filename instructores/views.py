from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import Instructor

# Create your views here.

def instructores(request):
    lista_instructores = Instructor.objects.all().values()
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