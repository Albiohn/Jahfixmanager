import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='alexisandres311@gmail.com',
    to_emails='alexisandres311@gmail.com',
    subject='Prueba SendGrid',
    html_content='<strong>¡Correo de prueba funcionando!</strong>'
)

try:
    sg = SendGridAPIClient("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")
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)
