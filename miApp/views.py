from django.http import HttpResponse
from django.shortcuts import render, redirect
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from .models import Empleado
from django import forms
from django.http import JsonResponse



class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'correo', 'rol']


def registro_empleado(request):
    print("La vista de registro_empleado fue llamada")  

    if request.method == 'POST':
        # Usar el formulario para validar los datos
        form = EmpleadoForm(request.POST)
        print("Formulario recibido:", request.POST)  # Muestra los datos recibidos
        
        if form.is_valid():
            print("Formulario válido. Guardando empleado...")
            form.save()
            # Redirigir al login
            return redirect('login')
        else:
            print("Errores en el formulario:", form.errors)  # Muestra los errores del formulario
            # Si los datos no son válidos, mostrar errores
            return JsonResponse({"error": form.errors}, status=400)

    # Si el formulario es GET, renderiza el formulario vacío
    form = EmpleadoForm()
    return render(request, 'miApp/registro.html', {'form': form})








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
