from django.contrib import admin
# Register your models here.
from .models import Usuarios, Peticion, Status, Disponibilidad

admin.site.register(Usuarios)
admin.site.register(Peticion)
admin.site.register(Disponibilidad)
admin.site.register(Status)