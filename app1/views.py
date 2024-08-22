from django.shortcuts import render

# Create your views here.
# views.py
from .models import Tarea
def ver_tareas_pendientes(request):
# Se interactúa con el modelo para obtener las tareas pendientes
    tareas_pendientes = Tarea.objects.filter(estado='pendiente')
# Se pasa la lista de tareas a la plantilla
    return render(request, 'pendientes.html', {'tareas': tareas_pendientes})
