from django.views.generic import ( ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView )
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Empleado


class InicioView(TemplateView):
    template_name='persona/list_all.html'

class ListAllEmpleados(ListView):
    template_name='persona/list_all.html'
    paginate_by= 4
    model=Empleado
    

class ListEmpleadosByDepartment(ListView):
    template_name='persona/list_by_department.html'

    def get_queryset(self):
        departamento = self.kwargs['department_short_name']
        lista = Empleado.objects.filter(departamento__short_name=departamento)
        return lista 
    

class ListEmpleadosByKeyword(ListView):
    template_name = 'persona/list_by_keyword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        keyword = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            Q(first_name=keyword) | Q(last_name=keyword)
        )
        return lista
    

class ListEmployeeAbilities(ListView):
    template_name= 'persona/list_abilities.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=3) # tarea hacer que este id se pase por url
        habilidades = empleado.habilidades.all()
        return habilidades
    

class EmpleadoDetaiView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"


class SuccessView(TemplateView):
    template_name= "persona/success.html"
    

class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    fields = ('__all__')
    success_url= reverse_lazy('persona_app:success')
    
    def form_valid(self, form):
        return super(EmpleadoCreateView, self).form_valid(form)
    

class EmpleadoUpdateView(UpdateView):
    template_name= "persona/update.html"
    model=Empleado
    fields = ('__all__')
    success_url= reverse_lazy('persona_app:success')


class EmpleadoDeleteView(DeleteView):
    template_name="persona/delete.html"
    model=Empleado
    success_url= reverse_lazy('persona_app:success')