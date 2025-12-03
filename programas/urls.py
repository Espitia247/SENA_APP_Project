from django.urls import path
from . import views 

app_name = 'programas'

urlpatterns = [
    # Ruta para la lista de programas
    path('programas/', views.programas, name='lista_programas'),
    
    # Ruta para el detalle de un programa (usando el ID como parámetro)
    path('programas/<int:programa_id>/', views.detalle_programa, name='detalle_programa'),
]