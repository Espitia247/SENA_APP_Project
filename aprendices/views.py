from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Aprendiz
from instructores.models import Instructor
# --- IMPORTAMOS EL MODELO PROGRAMA ---
from programas.models import Programa

# Create your views here.

def aprendices(request):
    lista_aprendices = Aprendiz.objects.all().values()
    template = loader.get_template('lista_aprendices.html')
    
    context = {
        'lista_aprendices': lista_aprendices,
        'total_aprendices': lista_aprendices.count(),
    }
    return HttpResponse(template.render(context, request))

def detalle_aprendiz(request, id_aprendiz):
    aprendiz = Aprendiz.objects.get(id=id_aprendiz)
    template = loader.get_template('detalle_aprendiz.html')
    context = {
        'aprendiz': aprendiz,
    }
    return HttpResponse(template.render(context, request))

def inicio(request):
    template = loader.get_template('main.html')
    
    # --- CALCULAMOS LOS TOTALES ---
    total_aprendices = Aprendiz.objects.count()
    total_instructores = Instructor.objects.count()
    total_programas = Programa.objects.count() # Nuevo total
    
    context = {
        'total_aprendices': total_aprendices,
        'total_instructores': total_instructores,
        'total_programas': total_programas, # Enviamos al template
    }
    return HttpResponse(template.render(context, request))