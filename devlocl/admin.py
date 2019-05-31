from django.contrib import admin
from django.contrib import admin
# Register your models here.
from .models import LocalUsers, Peticion, Status, Disponibilidad
from django.contrib.auth.admin import UserAdmin

class PersonalizadoUserAdmin(UserAdmin):
    fieldsets = ()
    add_fieldsets = (
        (None,{
            'fields':('usuario','password1','password2',),
        }),
    )
    list_display =('usuario','is_active','is_staff',)
    search_fields = ('usuario',)
    ordering = ('usuario',)

admin.site.register(LocalUsers,PersonalizadoUserAdmin)
admin.site.register(Peticion)
admin.site.register(Disponibilidad)
admin.site.register(Status)