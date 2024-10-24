from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)  # Category name (e.g., Medical Device)
    description = models.TextField(blank=True, null=True)  # Optional description for the category
    image = models.ImageField(upload_to='category/images/', blank=True, null=True)  # Image for the category
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the category was created

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)  # Name of the product
    description = models.TextField(blank=True, null=True)  # Short description of the product
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # ForeignKey to Category
    model_number = models.CharField(max_length=100,blank=True, null=True)  # Model or product number
    brochure = models.FileField(upload_to='products/brochures/', blank=True, null=True)  # PDF brochure
    specifications = models.TextField(blank=True, null=True)  # Key specifications of the product
    release_date = models.DateField(blank=True, null=True)  # Date the product was released
    price = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)  # Price of the product

    def __str__(self):
        return self.name
    
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')  # Reference to Product
    image = models.ImageField(upload_to='products/images/', null=True,blank=True)  # Image for the product
    alt_text = models.CharField(max_length=255, blank=True, null=True)  # Optional alt text for accessibility
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the image was added

    def __str__(self):
        return f"Image for {self.product.name}"