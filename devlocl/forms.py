from django import forms
from .models import LocalUsers, Peticion, Disponibilidad, Status


class SolitForm(forms.Form):
    class Meta:
        """Formulario de solicitud"""

        model = Peticion

        fields = [

            'solicitudes_id',
            'petit',
            'razon',
            'periodo_init',
            'periodo_fin',
            'dias_adicion',
            'horas_adicion',

        ]

        labels = {

            'solicitud_id':'Solicitud',
            'petit':'Tipo de Petición',
            'razon':'Razon',
            'periodo_init':'Rango de fecha inicial',
            'periodo_fin':'Fecha final',
            'dias_adicion':'Dias a adicionar, si es mas de 8 horas',
            'horas_adicion':'Horas a adiciona, si es menos de 1 dia',

        }
