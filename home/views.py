from django.shortcuts import render
from django.shortcuts import render, redirect
from contactus.forms import ContactForm


# Create your views here.
def index(request):
    
    contact_form =  ContactForm()

    context = {
        'contact_form': contact_form,
    }
    return render(request, 'home/index.html',context)