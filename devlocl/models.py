
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser, User
import datetime


#Modelo personalizado 
class Usuarios(AbstractUser):
    numero_empleado = models.IntegerField(null= True, blank= True)
    area = models.CharField(max_length = 200, null= True, blank= True)
    d_pendientes = models.IntegerField(null= True, blank= True)
    h_pendientes = models.IntegerField(null= True, blank= True)
    f_init = models.DateField(max_length = 200,null= True, blank= True)
    init_vac = models.DateField(max_length = 200, null= True, blank= True)
    fin_vac = models.DateField(max_length = 200, null= True, blank= True)
    ul_vac_tomadas = models.IntegerField(null= True, blank= True)


class Peticion(models.Model):
    solit_choices = (
        ('Adicionar','Adicionar'),
    )
    solicitudes_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, null=True, blank=True)
    petit = models.CharField(max_length = 255, choices=solit_choices, null=True, blank=False)
    fec = models.DateTimeField(auto_now=True)
    razon = models.TextField(max_length=255, null=True, blank=True)
    periodo_init = models.DateField(max_length = 200, null=True, blank=True)
    periodo_fin = models.DateField(max_length = 200, null=True, blank=True)
    dias_adicion = models.IntegerField(null=True, blank=False)
    horas_adicion = models.FloatField(null=True, blank=False)

        


class Disponibilidad(models.Model):
    solit_choices = (
        ('Disponer','Disponer'),
        ('Vacaciones','Vacaciones')
    )
    disponed_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, null=True, blank=True)
    disponsicion = models.CharField(max_length = 255, choices=solit_choices, null=True, blank=False)
    fec = models.DateTimeField(auto_now=True)
    razon_2 = models.TextField(max_length=255, null=True, blank=True)
    periodo_i = models.DateField(max_length = 200, null=True, blank=False)
    periodo_f = models.DateField(max_length = 200, null=True, blank=False)
    dias_disponer = models.IntegerField(null=True, blank=False)
    horas_disponer = models.FloatField(null=True, blank=False)
            
   
class Status(models.Model):
    stats_choices = (
        ('Aprobar','Aprobar'),
        ('Declinar', 'Declinar'),
    )
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, null=True, blank=True)
    solicitudes_id = models.ManyToManyField('Peticion')
    disponed_id = models.ManyToManyField('Disponibilidad')
    stats = models.CharField(max_length = 255, choices=stats_choices, null=True, blank=True)
    fecha_act = models.DateTimeField(auto_now=True)
