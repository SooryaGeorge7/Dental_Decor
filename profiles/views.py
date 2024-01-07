from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from reviews.models import Review
from .forms import UserProfileForm
from django.contrib import messages
from checkout.models import Order
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Profile updated successfully'
            )
        else:
            messages.error(
                request,
                'Update failed. Please ensure the form is valid.'
            )
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()
    user_reviews = Review.objects.filter(user=request.user)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'user_reviews':user_reviews,
        'on_profile_page': True,
        'profile': profile
    }

    return render(request, template, context)


def order_history(request, order_number):
    ''' Renders checkout success page '''
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
