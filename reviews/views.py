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

@login_required
def edit_review(request, review_id):
    
    review = get_object_or_404(Review, id=review_id)
    product = review.product
    reviews = Review.objects.filter(product=product)

    if request.method == 'POST':
        rating_form = RatingForm(request.POST, instance=review)
        if rating_form.is_valid():
            product_rating = rating_form.save(commit=False)
            product_rating.save()
            messages.success(request, "Review updated successfully.")
            return redirect('product_detail', product_id=product.id)
        else:
            messages.error(request, "Error updating the review. Please check the form.")
    else:
        rating_form = RatingForm(instance=review)

    user_reviewed = False
    if request.user.is_authenticated:
        user_review = Review.objects.filter(
            product=product, user=request.user
        )
        if user_review.exists():
            user_reviewed = True

    context = {
        'product': product,
        'rating_form': rating_form,
        'reviews': reviews,
        "user_reviewed": user_reviewed,
    }

    return render(request, 'reviews/edit_review_modal.html', context)
         
@login_required()
def delete_review(request,  review_id):
    """
    This function handles deleting of review for a particular restaurant.
    """
    user = request.user
    review = get_object_or_404(Review, id=review_id)
    product = review.product
    review.delete()
    messages.success(
            request,
            f"Your review for {product.name} has been deleted {user.username}"
        )

    return redirect('product_detail', product_id=product.id)