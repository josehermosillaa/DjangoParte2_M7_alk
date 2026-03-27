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


# Comandos ORM
Suponiendo que tenemos implementado un modelo Cliente en Django
```
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre}-{self.email}"
```

## Operaciones CRUD

### comandos para crear un dato (CREATE)

importante debe importar los modelos del archivo models para que sean utilizados

``` from clientes.models import Cliente```

```
Cliente.objects.create(nombre='Diego Castro', edad=24, email ="DG@gmail.com")
```

### comando para obtener un dato  (READ)
lo que se hace en este caso es obtener el dato a traves de uno de sus atributos

* caso 1: busqueda con get
``` Cliente.objects.get(email='diego@example.com')```

me permite traer el valor que encuentra en la base de datos, para la tabla del modelo que 
coincida con el argumento entregado, SOLO FUNCIONA CON COLUMNAS DE DATOS UNICOS

* caso 2: busqueda con filter:

``` Cliente.objects.filter(edad=24) ```

este codigo me trae todas las filas que coinciden con edad =  24.

* caso 3 : encontrar todos los registros de un Model
``` Cliente.objects.all()```

! recordar que esto nos devuelve un iterable de python que debemos recorrer para obtener los datos deseados
por objeto


### Actualizar un registro (UPDATE)

para esto debemos obtener el registro o fila que queremos actualiza, lo buscamos a traves de un valor unico

``` diego = Cliente.objects.get(email='diego@example.com')```

luego de obtener el dato debemos actualizar el atributo que queremos, para eso hacemos uso de las caracteristicas de los objetos en Python

``` diego.edad = 26 ```  
esto actualizaria la edad de diego de 24 a 26 años

``` diego.nombre = 'Juan Caros' ```
esto actualizaria el nombre

! ojo para que se apliquen estos cambios debemos ejecutar el metodo de guardado, este metodo viene de los modelos de django

```diego.save()``` 

ejemplo completo:
```
 diego = Cliente.objects.get(email='diego@example.com')
 diego.edad = 26  
 diego.save()
```

### Borrar un registro (DELETE)
buscamos la fila a borrar y aplicamos el metodo delete()

```
 diego = Cliente.objects.get(email='diego@example.com')
 diego.delete()
```


### Ejercicios

1. Obtener todos los clientes

    R: ``` Cliente.objects.all()  ```

2. Clientes mayores de 30

    R: ``` Cliente.objects.filter(edad__gt = 30) ```

    gt es greather than o mayor que 
    si queremos mayor o igual que, usamos la misma sintaxis pero con gte(greater than equal)

3. Clientes menores de 25

    R: ```Cliente.objects.filter(edad__lt = 25) ```
    lt es less than o menor que 
    si queremos menor o igual que, usamos la misma sintaxis pero con lte(less than equal)

4. busqueda por nombre

    * busqueda directa o exacta

    ``` Cliente.objects.filter(nombre = 'Ana Perez')```

    * podemos buscar por un texto contenido en el nombre
    ``` Cliente.objects.filter(nombre__contains='Ana') ```

    podria por ejemplo buscar nombres que contengan la letra a

    ``` Cliente.objects.filter(nombre__contains='a') ```
    el problema de contains es que es una busqueda exacta del texto en el nombre o campo filtrado, debe respetar mayusculas.

    si queremos buscar un texto sin importar quer este en mayuscula usamos icontains (insensitive)
    ``` Cliente.objects.filter(nombre__icontains='ana') ```


5. ordenar por edad (asc y desc)
    para ordenar de manera ascendente
    ``` Cliente.objects.oder_by("edad")```
    
    de manera deescendente
    ``` Cliente.objects.oder_by("-edad")```

    
6. contar clientes

    ``` Cliente.objecst.count() ```