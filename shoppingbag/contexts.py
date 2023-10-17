from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def shoppingbag_contents(request):
    shoppingbag_items = []
    total = 0
    product_count = 0

    shoppingbag = request.session.get('shoppingbag', {})

    for item_id, quantity in shoppingbag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        shoppingbag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })
    
    context = {
        'shoppingbag_items': shoppingbag_items,
        'total': total,
        'product_count': product_count,
    }

    return context

