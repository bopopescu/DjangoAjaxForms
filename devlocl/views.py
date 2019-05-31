from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import LocalUsers, Peticion, Disponibilidad, Status
from django.contrib.auth.models import User
from .forms import SolitForm
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
def solit(request):
    """Gestion de solicitudes"""
    if request.method == 'POST':
        form = SolitForm(request.POST, instance=request.user)
        if form.is_valid():
            LocalUsers.object.get(pk=form.cleaned_data['request.user'])
            form.cleaned_data['d_pendientes'] = form.cleaned_data['dias_adicion'] + form.cleaned_data['d_pendientes']
            form.save()
            subject = 'Welcome {}'.format(request.user)
            args = {'user': request.user}
            from_email = 'jadamson@super99.com'
            html_content = render_to_string('plantillas/send_mail.html', {'user':request.user})
            msg = EmailMultiAlternatives(subject, html_content, from_email, ['jadamson@super99.com'])
            msg.attach_alternative(html_content, 'plantillas/send_mail.html')
            msg.send()
        return redirect('send')
    else:
        form = SolitForm(instance=request.user)
        args = {'form':form}
    return render(request, 'plantillas/adicionar.html', args)
    
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


def adicion(request):
    """Gestion de solicitudes"""
    if request.method == 'POST':
        form2 = Sumaform(request.POST)
        if form2.is_valid():
            form.save()
            subject = 'Welcome {}'.format(request.user)
            from_email = 'jadamson@super99.com'
            html_content = render_to_string('plantillas/send_mail.html', {'user':request.user})
            msg = EmailMultiAlternatives(subject, from_email, ['jadamson@super99.com'])
            msg.attach_alternative(html_content, 'plantillas/send_mail.html')
            msg.send()
        return redirect('send')
    else:
        form2 = Sumaform(request.POST)
    return render(request, 'plantillas/solicitudes.html', {'form2':form2})
