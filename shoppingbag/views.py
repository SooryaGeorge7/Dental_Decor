
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.
def view_shoppingbag(request):
    
    return render(request, 'shoppingbag/shoppingbag.html')

def add_to_shoppingbag(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    shoppingbag = request.session.get('shoppingbag', {})
    
    if size:
        if item_id in list(shoppingbag.keys()):
            if size in shoppingbag[item_id]['items_by_size'].keys():
                shoppingbag[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {shoppingbag[item_id]["items_by_size"][size]}')
            else:
                shoppingbag[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
        else:
            shoppingbag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
    else:
        if item_id in list(shoppingbag.keys()):
            shoppingbag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {shoppingbag[item_id]}')
        else:
            shoppingbag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your shoppingbag')


    request.session['shoppingbag'] = shoppingbag
    
    return redirect(redirect_url)

def update_shoppingbag(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    shoppingbag = request.session.get('shoppingbag', {})

    if size:
        if quantity > 0:
            shoppingbag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {shoppingbag[item_id]["items_by_size"][size]}')
        else:
            del shoppingbag[item_id]['items_by_size'][size]
            if not shoppingbag[item_id]['items_by_size']:
                shoppingbag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            shoppingbag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {shoppingbag[item_id]}')
        else:
            shoppingbag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['shoppingbag'] = shoppingbag
    return redirect(reverse('view_shoppingbag'))

def remove_from_shoppingbag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        shoppingbag = request.session.get('shoppingbag', {})

        if size:
            del shoppingbag[item_id]['items_by_size'][size]
            if not shoppingbag[item_id]['items_by_size']:
                shoppingbag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
        else:
            shoppingbag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['shoppingbag'] = shoppingbag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

 
