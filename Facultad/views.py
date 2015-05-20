from .models import Facultad
from django.views.generic import ListView,CreateView,DeleteView,UpdateView,DetailView
from .forms import FormularioFacultad

#vista basada en clase para crear un objecto
#propiedades de la clase
#model=modelo a crear,eliminar.editar o visualizar dependiendo el tipo de clase
#template_name= plantilla donde se mostrara la vista
#fields=necesrio para crear y editar una vista muestra un formulario con los atributos que se le indican dentro
#success_url=redirecciona a la url que se le indica
#form_class= formulario de la archivo form

class CrearFacultad(CreateView):
    model = Facultad
    template_name = 'createview.html'
    form_class = FormularioFacultad
    success_url = "/"

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
    success_url = "/"

#actualizar un modelo
class ActualizarFacultad(UpdateView):
    template_name = 'updateview.html'
    model=Facultad
    form_class = FormularioFacultad
    success_url = "/"



