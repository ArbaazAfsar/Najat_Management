from django.urls import path
from . import views

urlpatterns = [
   
    path('all_products', views.all_products, name='all_products'),
    path('categories/', views.categories, name='categories'),
    path('categories/<int:category_id>/', views.products, name='products'),    
    path('products/<int:product_id>/', views.product_details, name='product_details'),
    path('product-management/', views.product_management, name='product_management'),    
    
 
]