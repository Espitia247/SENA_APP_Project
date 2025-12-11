from django.urls import path
from . import views 

app_name = 'programas'

urlpatterns = [
    # Ruta principal
    path('', views.main, name='main'),

    # Listar
    path('programas/', views.programas, name='lista_programas'),
    
    # Detalle
    path('programas/detalle/<int:programa_id>/', views.detalle_programa, name='detalle_programa'),

    # Crear
    path('programas/crear/', views.crear_programa, name='crear_programa'),

    # Editar
    path('programas/editar/<int:programa_id>/', views.editar_programa, name='editar_programa'),

    # Eliminar
    path('programas/eliminar/<int:programa_id>/', views.eliminar_programa, name='eliminar_programa'),
]