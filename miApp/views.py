from django.http import HttpResponse
from django.shortcuts import render, redirect
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from .models import Empleado


def registro_empleado(request):
    print("La vista de registro_empleado fue llamada")  # Esto ayudará a ver si la vista se ejecuta

    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        rol = request.POST.get('rol')

        # Crear un nuevo empleado en la base de datos
        Empleado.objects.create(
            nombre=nombre,
            apellido=apellido,
            correo=correo,
            rol=rol
        )

        # Redirigir al login después de registrar el empleado
        return redirect('login')

    # Renderizar el formulario de registro cuando la solicitud es GET
    return render(request, 'miApp/registro.html')








def notificacion(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')

        contenido = f"""
        <h2>Nuevo mensaje de contacto</h2>
        <p><strong>Nombre:</strong> {nombre}</p>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Mensaje:</strong><br>{mensaje}</p>
        """

        message = Mail(
            from_email='alexisandres311@gmail.com',
            to_emails='alexisandres311@gmail.com',
            subject='Formulario de Contacto - Django',
            html_content=contenido
        )

        try:
            sg = SendGridAPIClient("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")
            response = sg.send(message)
            return HttpResponse(f'Correo enviado. Código: {response.status_code}')
        except Exception as e:
            return HttpResponse(f'Error al enviar el correo: {str(e)}')

    return render(request, 'miApp/notificacion.html')








def index(request):
    return render(request, 'miApp/index.html')

def clientes(request):
    return render(request, 'miApp/clientes.html')

def dashboard(request):
    return render(request, 'miApp/dashboard.html')

def etapas(request):
    return render(request, 'miApp/etapas.html')

def login(request):
    return render(request, 'miApp/login.html')

def reparacion_detalle(request):
    return render(request, 'miApp/reparacion_detalle.html')

def seguimiento(request):
    return render(request, 'miApp/seguimiento.html')

def cotizacion(request):
    return render(request, 'miApp/cotizacion.html')
def cotizacionin(request):
    return render(request, 'miApp/cotizacionin.html')


def reparaciones(request):
    return render(request, 'miApp/reparaciones.html')
