from django.shortcuts import render, redirect
from .models import departamento, empleado
# Create your views here.

def list_departamentos(request):
    dep = departamento.objects.all()
    #print(dep)
    return render(request, 'departamentos.html', {"departamentos":dep})

def crear_departamento(request):
    #print(request.POST)
    dep = departamento(codigo=request.POST['codigo'], nombre=request.POST['nombre'], presupuesto=request.POST['presupuesto'])
    dep.save()
    return redirect('/departamentos')

def eliminar_departamento(request, dep_id):
    dep = departamento.objects.get(codigo=dep_id)
    dep.delete()
    return redirect('/departamentos')

def list_empleado(request):
    emp = empleado.objects.all()
    #print(emp)
    return render(request, 'personal.html', {"empleado":emp})

def crear_empleado(request):
    #print(request.POST)
    emp = empleado(codigo=request.POST['codigo'], codigo_departamento=request.POST['codigo_dep'] ,nif=request.POST['nif'],
                   nombre=request.POST['nombre'], apellido1=request.POST['apellido1'],apellido2=request.POST['apellido2'])
    emp.save()
    return redirect('/personal/emp')

def eliminar_empleado(request, emp_id):
    dep = empleado.objects.get(codigo=emp_id)
    dep.delete()
    return redirect('/personal/emp')

    


