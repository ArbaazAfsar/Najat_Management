from django.shortcuts import render,redirect,get_object_or_404
from .models import Product, Category
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.


def all_products(request):
    products = Product.objects.all()
    return render(request, 'all_products.html', {'products': products})

def categories(request):
    categories = Category.objects.all()  # Fetch all categories
    return render(request, 'categories.html', {'categories': categories})

def products(request, category_id):
    category = get_object_or_404(Category, id=category_id)  # Get the specific category
    products = category.product_set.all()  # Fetch products related to the category
    return render(request, 'products.html', {'category': category, 'products': products})

def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Get the specific product
    return render(request, 'product_details.html', {'product': product})


def product_management(request):
    # Admin-only view logic here
    return render(request, 'product_management.html')