from django.shortcuts import render
from .forms import RatingForm
from .models import Review
from products.models import Product
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def addreview(request):
    
    return render(request, 'review/review_page.html', context)