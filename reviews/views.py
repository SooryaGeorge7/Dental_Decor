from django.shortcuts import render
from .forms import RatingForm
from .models import Review
from products.models import Product
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        rating_form = RatingForm(request.POST)
        if rating_form.is_valid():
            review = rating_form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            messages.success(request, f"Your review for {product.name} has been submitted.")
        else:
            messages.error(request, "Error submitting the review. Please check the form.")

    return redirect('product_detail', product_id=product_id)