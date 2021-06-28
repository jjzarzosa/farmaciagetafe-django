from django.shortcuts import render
from store.models import Product, ReviewRating

def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('fecha_alta')

    # Get the reviews
    print("error1")
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
    print("error2")
    context = {
        'products': products,
        'reviews': reviews,
    }
    return render(request, 'home.html', context)