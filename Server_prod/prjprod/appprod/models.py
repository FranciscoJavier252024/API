from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=250, default="0")
    precio = models.DecimalField(max_digits=10, decimal_places=2, default="0")
    existencias = models.IntegerField(default="0")

    def __str__(self):
        return f"{self.nombre} (ID: {self.id})"