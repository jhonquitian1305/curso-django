from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView

from applications import departamento

from .forms import NewDepartamentoForm
from applications.persona.models import Empleado
from .models import Departamento

# Create your views here.


class DepartamentoListView(ListView):
    template_name = "departamento/lista.html"
    model = Departamento
    context_object_name = 'departamentos'

class NewDapartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        print('*************Estamos en el form valid***************')
        dep = Departamento(
            name = form.cleaned_data['departamento'],
            short_name = form.cleaned_data['shortname'],
        )        
        dep.save()
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name =  nombre,
            last_name = apellido,
            job = '1',
            departamento = dep
        )
        return super(NewDapartamentoView, self).form_valid(form)