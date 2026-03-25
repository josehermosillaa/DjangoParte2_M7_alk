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

Django posee tambien comandos para filtrar en el ORM
* gt : greater than, mayor que ```Producto.objects.filter(precio__gt=100)``` 
* lt: less than, menor que ```Producto.objects.filter(precio__lt=100)``` 
* gte : greater than equal, mayor o igual que ```Producto.objects.filter(precio__gte=100)```
* * lt: less than, meno o igual que ```Producto.objects.filter(precio__lte=100)``` 

### Ordenamiento
se pueden ordenar por un campo  a partir de 
* ```Producto.objects.order_by('nombre')``` ascendente
* ```Producto.objects.order_by('-nombre')``` descendente
  

### para concatenar consultas
``` from django.db.models import Q
productos = Producto.objects.filter(Q(precio__gt=50) & Q(stock__gte=10)) ```


## cambiar la shell de python a Ipython
instalamos ipython con el entorno virtual activado

``` pip install ipython```
y luego corremos en el proyecto la terminal con 
``` python manage.py shell -i ipython ```