from django.shortcuts import render, redirect, get_object_or_404
from .models import Programa
from .forms import ProgramaForm # Asegúrate de importar el formulario

# --- VISTA PRINCIPAL ---
def main(request):
    return render(request, "main.html")

# --- LISTAR ---
def programas(request):
    # OJO: Quité el .values() para que funcionen los métodos get_display en el HTML
    lista_programas = Programa.objects.all() 
    context = {
        "programas": lista_programas, # Cambié la clave a 'programas' para que coincida con tu HTML
        'total_programas': lista_programas.count(),
    }
    return render(request, "lista_programas.html", context)

# views.py

def detalle_programa(request, programa_id):
    programa = get_object_or_404(Programa, id=programa_id)
    context = {
        "programa": programa, 
    }
    return render(request, "detalle_programa.html", context)

# --- CREAR ---
def crear_programa(request):
    if request.method == 'POST':
        form = ProgramaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('programas:lista_programas') # Redirige a la lista
    else:
        form = ProgramaForm()

    return render(request, 'crear_programa.html', {'form': form})

# --- EDITAR ---
def editar_programa(request, programa_id):
    programa = get_object_or_404(Programa, id=programa_id)
    
    if request.method == 'POST':
        form = ProgramaForm(request.POST, instance=programa)
        if form.is_valid():
            form.save()
            return redirect('programas:lista_programas')
    else:
        form = ProgramaForm(instance=programa) # Carga los datos existentes

    return render(request, 'editar_programa.html', {'form': form})

# --- ELIMINAR ---
def eliminar_programa(request, programa_id):
    programa = get_object_or_404(Programa, id=programa_id)
    
    if request.method == 'POST':
        programa.delete()
        return redirect('programas:lista_programas')
        
    return render(request, 'eliminar_programa.html', {'programa': programa})