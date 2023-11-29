from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, reverse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Wishlist
from products.models import Product
from django.contrib import messages

@login_required
def wishlist(request):
    wish_items = Wishlist.objects.filter(user=request.user)

    context = {
        'wish_items': wish_items,
        
    }
    

    return render(request, 'wishlist/wishlist.html', context)

def add_to_wishlist(request, product_id):
    
    product = get_object_or_404(Product, id=product_id)
    try:
        wish_item = Wishlist.objects.get(user=request.user, product=product)
        messages.info(request, f'{product.name} is already in your wishlist.')
    except Wishlist.DoesNotExist:
        Wishlist.objects.create(user=request.user, product=product)
        messages.success(request, f'{product.name} added to wishlist')
           

    return redirect('product_detail', product_id=product.id)

def remove_from_wishlist(request, product_id):
    
    product = get_object_or_404(Product, id=product_id)
    print(product)
    wish_item = Wishlist.objects.get(user=request.user, product=product)
    print(wish_item)

    if request.method == 'POST':
        wish_item.delete()
        messages.success(request, f'{product.name} removed from your wishlist.')

    return redirect('wishlist')