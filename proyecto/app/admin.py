from django.contrib import admin
from .models import Producto, Categoria, Perfil

# Register your models here.

#puede customizar el panel de admin
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Perfil)