from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Usuarios, Peticion, Disponibilidad, Status
from django.contrib.auth.models import User, AbstractUser
from .forms import addiForm
import json 
from django.http import JsonResponse
from django.urls import reverse
# Create your views here.


@login_required
def index(request):
    """Datos del UsrDentro"""
    args = {'user': request.user}
    return render(request, "plantillas/base.html", args)

    
        
def report(request):
    obj = Usuarios.objects.all()
    for abc in obj:
        obj_user = abc.usuario
        obj_nu_empleado = abc.numero_empleado
        obj_nombres = abc.nombre
        obj_apellidos = abc.apellido
        obj_area = abc.area
        obj_fec_nac = abc.f_nac
        obj_diasp = abc.d_pendientes
        obj_horasp = abc.h_pendientes
        obj_fechai = abc.f_init
        obj_iniciov = abc.init_vac
        obj_finv = abc.fin_vac
        obj_ulvac = abc.ul_vac_tomadas
        
    context = {
        "obj":obj,
        "obj_user":obj_user,
        "obj_nu_empleado":obj_nu_empleado,
        "obj_nombres":obj_nombres,
        "obj_apellidos":obj_apellidos,
        "obj_area":obj_area,
        "obj_fec_nac":obj_fec_nac,
        "obj_diasp":obj_diasp,
        "obj_horasp":obj_horasp,
        "obj_fechai":obj_fechai,
        "obj_iniciov":obj_iniciov,
        "obj_finv":obj_finv,
        "obj_ulvac":obj_ulvac,
    }
    return render(request,"plantillas/reporte.html", context)       
#Pagina de reporte

def solit(request):
    if request.method == 'POST' and request.is_ajax():
        form = addiForm(request.POST)
        if form.is_valid():
            peticion = form.save(commit=False)
            if peticion.usuario:
                peticion.usuario = request.user
                peticion.save()
                peticion.usuario.d_pendientes = form.cleaned_data.POST.get('dias_adicionar', None)  # Get the form value if has, otherwise assign it to None (change it if you want another default value)
                peticion.usuario.h_pendientes = form.cleaned_data.POST.get('horas_adicionar', None)  # The same
                peticion.usuario.save()            
            return JsonResponse({'status': 'true', 'msg': 'Procesado Correctamente'})
        else:
            return JsonResponse({'status': 'false', 'msg': 'Los datos no son validos'})

    form = addiForm()
    return render(request, 'plantillas/adicionar.html', {'form':form})

     
#Pagina de solicitudes
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect ('index')
        else:
            return render (request, 'registration/login.html',{'error':'Vuelva a intentarlo'})
    return render (request, 'registration/login.html')
#LoginPage


def logout_view(request):
    """Logout"""
    logout(request)
    return redirect("login_view")
#Log outPage 

def send_view(request):
    """Hoja de exito"""
    return render(request, 'plantillas/sendview.html')


