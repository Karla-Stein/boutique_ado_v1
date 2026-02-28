from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def all_products(request):
    """
    A view to show all products, including sorting and search queries.
    """
    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            # splits categories into a python list
            categories = request.GET['category'].split(',')
            # checks if the category is in the python list
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(
                    description__icontains=query)
            products = products.filter(queries)

    return render(
        request,
        'products/products.html',
        {'products': products,
         'search_term': query,
         'current_categories': categories,
         }
    )


def product_detail(request, product_id):
    """
    A view to show individual product details.
    """
    # to get a single object, not a query set
    product = get_object_or_404(Product, pk=product_id)

    return render(
        request,
        'products/product_detail.html',
        {'product': product, }
    )
