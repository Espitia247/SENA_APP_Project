from django.urls import path
from . import views

app_name = 'instructores'

urlpatterns = [
    path('instructores/', views.instructores, name='lista_instructores'),
    path('instructores/instructor/<int:id_instructor>/', views.detalle_instructor, name='detalle_instructor'),
    path('instructores/crear/', views.InstructorCreateView.as_view(), name='crear_instructor'),
    path('instructores/<int:instructor_id>/editar/', views.InstructorUpdateView.as_view(), name='editar_instructor'),
    path('instructores/<int:instructor_id>/eliminar/', views.InstructorDeleteView.as_view(), name='eliminar_instructor'),
]