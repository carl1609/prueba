from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

path('tareas/pendientes/', views.ver_tareas_pendientes, name='ver_tareas_pendientes'),
path('tareaview/',views.TareaView.as_view(),name='repuesta_tarea'),
path('formulariotarea/',views.crear_tarea,name="crear_tarea")

]
