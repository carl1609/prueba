from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

path('tareas/pendientes/', views.ver_tareas_pendientes, name='ver_tareas_pendientes'),

]
