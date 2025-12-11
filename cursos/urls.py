from django.urls import path
from . import views

app_name = 'cursos'

urlpatterns = [
    path('', views.cursos, name='lista_cursos'),
    path('curso/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
    path('crear/', views.CursoCreateView.as_view(), name='crear_curso'),
    path('editar/<int:curso_id>/', views.CursoUpdateView.as_view(), name='editar_curso'),
    path('eliminar/<int:curso_id>/', views.CursoDeleteView.as_view(), name='eliminar_curso'),
]