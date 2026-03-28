from django.db import models

# Create your models here.
class Cliente(models.Model):
    #id numero entero secuencial
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField(unique=True)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)
    def __str__(self):
        return f"{self.nombre}-{self.email}"
    


class Producto(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre =models.CharField(max_length=150)

    def __str__(self):
        return self.nombre
    

class Tienda(models.Model):
    nombre = models.CharField(max_length = 100)
    direccion = models.TextField() #
    # direccion = models.TextField(unique=True) #my sql no permite caracteres de texto unicos si es que no tienen un largo definido
    abierto = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre} - {self.direccion}'
    


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    anio_publicacion = models.IntegerField(default=2000)
   