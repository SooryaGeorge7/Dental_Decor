from django.shortcuts import render, redirect
from contactus.forms import ContactForm
from profiles.models import UserProfile


def index(request):
    '''
    A view to render the home page
    '''
    if  request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        contact_form = ContactForm(initial={'email': profile.user.email})
    else:
        contact_form = ContactForm()
    context = {
        'contact_form': contact_form,
    }
    return render(request, 'home/index.html', context)
