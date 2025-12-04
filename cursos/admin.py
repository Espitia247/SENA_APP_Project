from django.contrib import admin
from .models import Curso, InstructorCurso, AprendizCurso    

admin.site.register(Curso)
admin.site.register(InstructorCurso)
admin.site.register(AprendizCurso)  


# Register your models here.
