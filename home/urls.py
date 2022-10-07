from venv import create
from django.urls import path
from .views import *

urlpatterns = [
    path('',list_departamentos),
    path('new/',crear_departamento, name='crear_dep'),
    path('elimi/<int:dep_id>/',eliminar_departamento, name='elim_dep'),
    path('emp/',list_empleado),
    path('nuevo/',crear_empleado, name='crear_emp'),
    path('elim/<int:emp_id>',eliminar_empleado, name='elim_emp'),
    
    
]
