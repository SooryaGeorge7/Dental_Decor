from django.shortcuts import (render, redirect,
                              reverse, get_object_or_404)
from django.contrib import messages
from .models import Product, Category
from django.db.models.functions import Lower
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from reviews.forms import RatingForm
from reviews.models import Review
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def shop_products(request):
    '''
    Render all products on products page
    '''
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(
                    lower_name=Lower('name')
                )

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(
                category__name__in=categories
                )
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                )
                return redirect(reverse('shop_products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'
    products_count = products.count()

    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        page_number = 1
        products = paginator.page(page_number)
    except EmptyPage:
        page_number = paginator.num_pages
        products = paginator.page(page_number)

    

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'products_count':products_count,
        'page_number':page_number,
    }

    return render(request, 'products/shop_products.html', context)


def product_detail(request, product_id):
    '''
    Render product details page
    '''
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)
    rating_form = RatingForm()
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

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store owners can do that.'
        )
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(
            request.POST, request.FILES, instance=product
            )
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please \
                ensure the form is valid.'
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store owners can do that.'
        )
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('shop_products'))
