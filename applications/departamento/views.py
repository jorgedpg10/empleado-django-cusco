from django.views.generic.edit import FormView

from .forms import NewDepartamentoForm
from applications.persona.models import Empleado
from .models import Departamento

class NewDepartamentoView(FormView):
    template_name= 'departamento/new_departamento.html'
    form_class= NewDepartamentoForm
    success_url= '/'

    def form_valid(self, form):

        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']

        dep = Departamento(
            name = form.cleaned_data['departamento'],
            short_name = form.cleaned_data['short_name'],
        )

        dep.save()

        emp = Empleado.objects.create(
            first_name=nombre, 
            last_name=apellidos,
            job="administrador",
            departamento= dep,
            
            )
        Emp.save()
        return super(NewDepartamentoView, self).form_valid(form)