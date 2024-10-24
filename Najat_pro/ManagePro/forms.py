from django import forms
from products.models import Product,Category,ProductImage

# Existing Product Form
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'model_number', 'brochure', 'specifications', 'release_date', 'price']

# New Form for Product Images
class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image', 'alt_text']  # Fields for the product image
        
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'image']