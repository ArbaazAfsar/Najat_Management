from django.contrib import admin
from .models import Product, Category, ProductImage

# Inline class to add images directly in the Product admin page
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 5  # Number of empty image forms to display

# Admin class for the Product model
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'model_number', 'price', 'release_date')  # Fields to display in the admin list view
    search_fields = ('name', 'model_number')  # Fields that can be searched
    list_filter = ('category', 'release_date')  # Filters for the right sidebar
    inlines = [ProductImageInline]  # Inline for adding images directly in the Product admin page

# Admin class for the Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')  # Fields to display in the category list
    search_fields = ('name',)  # Field that can be searched
    list_filter = ('created_at',)  # Filter categories by created date

# Register the models with their custom admin classes
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductImage)
