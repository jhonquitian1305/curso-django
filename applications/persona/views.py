from random import choices
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)

# models
from .models import Empleado
# Create your views here.

class InicioView(TemplateView):
    """ Vista que carga la página de inicio"""
    template_name = 'inicio.html'


class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    ordering = 'id'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            full_name__icontains = palabra_clave
        )
        return lista


class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    ordering = 'id'
    context_object_name = 'empleados'
    model = Empleado


class ListByAreaEmpleado(ListView):
    """ Lista empleados de un área """    
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'
    # Una forma no recomendable
    # queryset = Empleado.objects.filter(
    #     departamento__short_name = 'otro'
    # )

    # Una mejor forma para listar
    def get_queryset(self):
        area = self.kwargs['shortname']
        lista = Empleado.objects.filter(
            departamento__short_name = area
        )
        return lista


    # Listar empleado por trabajo(pendiente)
class ListByJobEmpleado(ListView):
    """ Listar Empleados por trabajo"""
    template_name = 'persona/list_by_job.html'

    def get_queryset(self):
        trabajo = self.kwargs['job']
        lista = Empleado.objects.filter(
            job = trabajo
        )
        return lista


class ListEmpleadosByKword(ListView):
    """ Listar empleados por palabra clave """
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('*************')
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        return lista


class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'
    
    def get_queryset(self):
        empleado = Empleado.objects.get(id=6)
        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context


class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        # lógica del proceso
        empleado = form.save(commit=False)
        empleado.full_name = f'{empleado.first_name} {empleado.last_name}'
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado

    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('*******************MÉTODO POST*******************')
        print('======================================')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print('*******************MÉTODO form valid*******************')
        print('**************************************')
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')
