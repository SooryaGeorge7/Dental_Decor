from django.shortcuts import render
from .models import Product

# Create your views here.
def shop_products(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/shop_products.html', context)