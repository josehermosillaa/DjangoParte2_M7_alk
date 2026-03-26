from django.db import models
from django.contrib.auth.models import User #modelo usuarios de Django
# Create your models here.


class Categoria(models.Model):
    #ID se crea automáticamente como clave primaria
    # id = models.AutoField(primary_key=True)#este comando al hacer primary_key=True sobre escribe el id automatico de Django
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) #aqui implicitamemte estoy diciendo que mcuhos productos tendran una misma categoria
    # N->1

    def __str__(self):
        return self.nombre



class Perfil(models.Model):
    """
    recordar que el modelo User de Django tiene los siguientes atributos
    username
    password
    email
    
    name last_name por comprobar
    """
    usuario = models.OneToOneField(User, on_delete=models.CASCADE) #relaciones uno a uno
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()    
    
    def __str__(self):
        return self.usuario.username +"-"+self.usuario.email
    
    
    