from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    # print('Tipo de petición: {}'.format(request.method)) # GET o POST
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')

            """ email = EmailMessage(
                asunto,
                cuerpo,
                email_origen,
                email_destino,
                reply_to=[email]
            ) """

            email = EmailMessage(
                'La Caffettiera: Nuevo mensaje',
                'De {} <{}>\n\nEscribió:\n\n{}'.format(name, email, message),
                'no-contestar@inbox.mailtrap.io',
                ['m.oviedo@uni.pe', 'moviedor05@gmail.com'],
                reply_to=[email]
            )
            try:
                email.send()
                # Si pasa la validación, enviamos un correo y redireccionamos
                return redirect(reverse('contact') + '?ok') # reverse: Django maneja el path de las urls dinámicamente
            except:
                # TODO:
                # Redireccionamos a FAIL
                return redirect(reverse('contact') + '?fail')

    return render(request, 'contact/contact.html', {'form': contact_form})