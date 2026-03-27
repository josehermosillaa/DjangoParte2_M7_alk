from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre}-{self.email}"
    


class Producto(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre =models.CharField(max_length=100)

    def __str__(self):
        return self.nombre