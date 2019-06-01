from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import LocalUsers, Peticion, Disponibilidad, Status
from django.contrib.auth.models import User
from .forms import addiForm, baseForm
# Create your views here.


@login_required
def index(request):
    """Datos del UsrDentro"""
    args = {'user': request.user}
    return render(request, "plantillas/base.html", args)

    
        
def report(request):
    obj = LocalUsers.object.all()
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

@login_required
def adicion(request):
    
    """Gestion de solicitudes"""
    if request.method == 'POST':
        form = addiForm(request.POST, instance=request.user)
        form2 = baseForm(request.POST, instance=request.user)
        if form.is_valid and form2.is_valid():
            form.save()
        return redirect ('send')
    
    else:
        form = addiForm(instance=request.user)
        args = {'form': form}
    return render (request, 'plantillas/adicionar.html', {'form':form}, args)
   
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


