from django.db import models

class Prueba(models.Model):
    titulo = models.CharField(max_length=60)
    subtitulo = models.CharField(max_length=60)
    cantidad = models.DecimalField(max_digits=5, decimal_places=0)

    def __str__(self):
        return self.titulo

  
