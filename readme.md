## Configuracion de MySQL
* recordar instalar mysqlclient en el entorno virtual
``` pip install mysqlclient```
* reemplazar esta configuracion en settings.py
``` 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mi_basedatos',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```  
## Ejemplos de comando ORM DJANGO
Asumimos que tenemos el modelo Producto creado
``` class Producto(models.Model):
        nombre = models.CharField(max_length=100)
        precio = models.DecimalField(max_digits=8, decimal_places=2)
        stock = models.IntegerField()

        def __str__(self):
            return self.nombre
```
recordar importar el modelo al archivo u terminal a utilizar
ejemplo la shell de Django
``` python manage.py shell ```
* podemos crear un nuevo producto con :
  ``` Producto.objects.create(nombre='Polera',precio='12990',stock='20')``` 

* seleccionar todos los datos del modelo
    ``` Producto.objects.all() ```