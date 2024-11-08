from django.db import models

from applications.departamento.models import Departamento

class Habilidad(models.Model):
    name = models.CharField(max_length=60)
    
    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"

    def __str__(self):
        return self.name


class Empleado (models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='empleado', blank=True, null=True )
    habilidades = models.ManyToManyField(Habilidad)

    def __str__(self):
        return self.first_name + self.last_name
    


