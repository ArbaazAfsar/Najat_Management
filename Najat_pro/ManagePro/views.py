from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from products.models import Product, Category, ProductImage
from .forms import ProductForm,CategoryForm, ProductImageForm
from django.contrib import messages
from django.forms import modelformset_factory

# Upload Product - Only for staff members
@staff_member_required
def upload_product(request):
    
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        
        # Use a formset for handling multiple product images
        ImageFormSet = modelformset_factory(ProductImage, form=ProductImageForm,)# extra=5)
        image_formset = ImageFormSet(request.POST, request.FILES, queryset=ProductImage.objects.none())
        
        if product_form.is_valid() and image_formset.is_valid():
            product = product_form.save()
            for form in image_formset:
                product_image = form.save(commit=False)
                product_image.product = product  # Associate the image with the product
                product_image.save()
            return redirect('all_products')  # Change to your success URL
    else:
        product_form = ProductForm()
        ImageFormSet = modelformset_factory(ProductImage, form=ProductImageForm, extra=5)
        image_formset = ImageFormSet(queryset=ProductImage.objects.none())

    context = {
        'product_form': product_form,
        'image_formset': image_formset,
    }
    return render(request, 'product_upload.html', context)




# Edit Product - Only for staff members
@staff_member_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('all_products')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'product_edit.html', {'form': form, 'product': product})

# Delete Product - Only for staff members
@staff_member_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('all_products')
    
    return render(request, 'product_delete.html', {'product': product})




# Upload Category - Only for staff members
@staff_member_required
def upload_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category uploaded successfully!')
            return redirect('categories')
    else:
        form = CategoryForm()
    
    return render(request, 'category_upload.html', {'form': form})

# Edit Category - Only for staff members
@staff_member_required
def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('edit_and_delete')  # Redirect after saving
    else:
        form = CategoryForm(instance=category)
    
    return render(request, 'edit_category.html', {'form': form, 'category': category})

# Delete Category - Only for staff members
@staff_member_required
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('edit_and_delete')  # Redirect after deletion
    
    return render(request, 'delete_category.html', {'category': category})


def edit_and_delete(request):
    categories = Category.objects.all()  # Fetch all categories
    return render(request, 'edit_and_delete.html', {'categories': categories})