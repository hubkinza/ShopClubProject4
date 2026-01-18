"""
URL patterns for products app
"""
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    
    # Products
    path('products/', views.product_list, name='product_list'),
    path('category/<slug:slug>/', views.category_products, name='category'),
    
    # Admin product management (MUST come BEFORE product_detail)
    path('product/create/', views.product_create, name='product_create'),
    path('product/<slug:slug>/edit/', views.product_edit, name='product_edit'),
    path('product/<slug:slug>/delete/', views.product_delete, name='product_delete'),
    
    # Product detail (comes AFTER specific routes)
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    
    # Cart
    path('cart/', views.cart, name='cart'),
    path('cart/add/<slug:slug>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:item_id>/', views.update_cart, name='update_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]