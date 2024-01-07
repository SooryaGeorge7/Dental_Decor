from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def shoppingbag_contents(request):
    '''
    Handles the shopping bag contents
    '''
    shoppingbag_items = []
    total = 0
    product_count = 0

    shoppingbag = request.session.get('shoppingbag', {})

    for item_id, item_data in shoppingbag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            shoppingbag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                shoppingbag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    context = {
        'shoppingbag_items': shoppingbag_items,
        'total': total,
        'product_count': product_count,
    }


    return context
