from django.contrib import admin
from .models import Facultad


#esta clase muestra la lista de facultades con cada uno no los atributos mencionados en su list_diplay
class FacultadAdmin(admin.ModelAdmin):
    list_display = ("codigo","nombre")

#registra un modelo para poder ser visualizado en el admin
admin.site.register(Facultad,FacultadAdmin)