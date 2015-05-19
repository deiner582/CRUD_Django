from .models import Facultad
from django.views.generic import ListView,CreateView,DeleteView,UpdateView,DetailView


#vista basada en clase para crear un objecto
#propiedades de la clase
#model=modelo a crear,eliminar.editar o visualizar dependiendo el tipo de clase
#template_name= plantilla donde se mostrara la vista
#fields=necesrio para crear y editar una vista muestra un formulario con los atributos que se le indican dentro
#success_url=redirecciona a la url que se le indica

class CrearFacultad(CreateView):
    model = Facultad
    template_name = 'createview.html'
    fields = ['codigo','nombre']
    success_url = "/lista"
    def form_valid(self, form):
        print("valido")
        return super(CrearFacultad,self).form_valid(form)

    def form_invalid(self, form):
        print("invalido")
        return super(CrearFacultad,self).form_invalid(form)

#listar todas las facultades
class ListaFacultad(ListView):
    template_name = 'listview.html'
    model = Facultad

#detalle de una facultad
class DetalleFacultad(DetailView):
    template_name = 'detailview.html'
    model = Facultad

#eliminar una facultad
class EliminarFacultad(DeleteView):
    template_name = 'deleteview.html'
    model=Facultad
    success_url = "/lista"

#actualizar un modelo
class ActualizarFacultad(UpdateView):
    template_name = 'updateview.html'
    model=Facultad
    fields = ['codigo','nombre']
    success_url = "/lista"



