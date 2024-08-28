from django.http import HttpRequest
from django.shortcuts import render
from django.views import View


# Create your views here.
# views.py
from .models import Tarea
def ver_tareas_pendientes(request):
# Se interactúa con el modelo para obtener las tareas pendientes
    tareas_pendientes = Tarea.objects.filter(estado='pendiente')
# Se pasa la lista de tareas a la plantilla
    return render(request, 'pendientes.html', {'tareas': tareas_pendientes})

def crear_tarea(request):
    contexto={
        'url':'http://localhost:8000/tareaview/',
        'estados':['pendiente','completado'] # type: ignore
    }

    return render(request,'crear_tarea.html',contexto)


class TareaView(View):
    def post(self,request):
        titulo=request.POST.get("titulo")
        descripcion=request.POST.get("descripcion")
        estado=request.POST.get("estado")

        if(titulo != "" and descripcion != "" and estado != "" ):
            nueva_tarea=Tarea(titulo=titulo,descripcion=descripcion,estado=estado)
            nueva_tarea.save()
            return HttpRequest("se envio guardo la tarea con exito",status=201)
        else:
            return HttpRequest("error parametros incompletos",estatus=400)
        
        
