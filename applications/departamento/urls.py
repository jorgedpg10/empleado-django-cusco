from django.urls import path

from . import views

urlpatterns = [
    path('departamento-crear/', views.NewDepartamentoView.as_view(), name='nuevo_departamento'),
]