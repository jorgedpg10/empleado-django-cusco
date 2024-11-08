from django.db import models

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50) # se mostrará 'Nombre' en el admin de dj
    short_name = models.CharField('Nombre Corto', max_length=20)
    active = models.BooleanField('Anulado', default=False)

    def __str__(self):
        return self.name + '-' + self.short_name
    
    