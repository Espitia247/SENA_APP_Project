from django.urls import path
from . import views

# Namespace para evitar conflictos con otras apps
app_name = 'cursos'

urlpatterns = [
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('cursos/curso/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
]