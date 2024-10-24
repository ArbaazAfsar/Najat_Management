from django.urls import path
from . import views




urlpatterns = [
    path('upload-category/', views.upload_category, name='upload_category'),
    path('edit_and_delete/', views.edit_and_delete, name='edit_and_delete'),
    path('edit_category/<int:category_id>/', views.edit_category, name='edit_category'),  # Edit category
    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),  # Delete category
    path('upload-product/', views.upload_product, name='upload_product'),
    path('edit-product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),

    
]