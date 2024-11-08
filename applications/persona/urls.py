from django.urls import path

from . import views 

app_name = "persona_app"

urlpatterns = [
    path('empleados/', views.ListAllEmpleados.as_view()),
    path('empleados-por-departamento/<department_short_name>', views.ListEmpleadosByDepartment.as_view()),
    path('buscar-empleado/', views.ListEmpleadosByKeyword.as_view()),
    path('lista-habilidades-empleado/', views.ListEmployeeAbilities.as_view()),
    path('empleado/<pk>/', views.EmpleadoDetaiView.as_view()),
    path('empleado-crear/', views.EmpleadoCreateView.as_view()),
    path('empleado-update/<pk>', views.EmpleadoUpdateView.as_view(), name="empleado-update"),
    path('empleado-delete/<pk>', views.EmpleadoDeleteView.as_view(), name="empleado-delete"),
    path('success/', views.SuccessView.as_view(), name="success")
]