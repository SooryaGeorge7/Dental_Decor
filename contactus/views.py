from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.urls import reverse
# Create your views here.
from django.core.mail import send_mail
from django.conf import settings


def contact_us(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_instance = form.save()
            subject = 'Confirmation Email'
            message = 'Thank you for your message. We will get back \
             to you soon!'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [contact_instance.email]

            send_mail(subject, message, from_email, to_email)
            messages.success(request, f'Your message was sent successfuly,\
             You will recieve an email confirmation message shortly')

        else:
            messages.error(request, f'There is an error found in the form')

    return redirect(reverse('home'))
