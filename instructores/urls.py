from django.urls import path
from . import views 

app_name = 'instructores'

urlpatterns = [
    path('instructores/', views.instructores, name='lista_instructores'),
    path('instructores/instructor/<int:id_instructor>/', views.detalle_instructor, name='detalle_instructores'),
    ]