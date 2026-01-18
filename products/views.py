"""
Views for products app
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Product, Category, Cart


def home(request):
    """Homepage with featured products and categories"""
    categories = Category.objects.all()[:6]
    featured_products = Product.objects.filter(available=True)[:8]
    
    context = {
        'categories': categories,
        'featured_products': featured_products,
    }
    return render(request, 'products/home.html', context)


def product_list(request):
    """Display all products with filters and sorting"""
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    
    # Category filter
    category_slug = request.GET.get('category')
    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    # Search filter
    search_query = request.GET.get('q')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    # Price filter
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    
    # Sorting
    sort_by = request.GET.get('sort', '-created_at')
    if sort_by in ['name', '-name', 'price', '-price', '-created_at']:
        products = products.order_by(sort_by)
    
    # Pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    
    context = {
        'products': products,
        'categories': categories,
        'category': category,
    }
    return render(request, 'products/product_list.html', context)


def category_products(request, slug):
    """Display products by category"""
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, available=True)
    categories = Category.objects.all()
    
    # Sorting
    sort_by = request.GET.get('sort', '-created_at')
    if sort_by in ['name', '-name', 'price', '-price', '-created_at']:
        products = products.order_by(sort_by)
    
    # Pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    
    context = {
        'products': products,
        'categories': categories,
        'category': category,
    }
    return render(request, 'products/product_list.html', context)


def product_detail(request, slug):
    """Display single product details"""
    product = get_object_or_404(Product, slug=slug)
    
    # Get related products from same category
    related_products = Product.objects.filter(
        category=product.category,
        available=True
    ).exclude(id=product.id)[:4]
    
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def cart(request):
    """Display user's shopping cart"""
    cart_items = Cart.objects.filter(user=request.user).select_related('product')
    
    # Calculate subtotal
    subtotal = sum(item.total_price for item in cart_items)
    total = subtotal  # no tax included
    
    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'total': total,
    }
    return render(request, 'products/cart.html', context)


@login_required
def add_to_cart(request, slug):
    """Add product to cart"""
    if request.method == 'POST':
        product = get_object_or_404(Product, slug=slug)
        quantity = int(request.POST.get('quantity', 1))
        
        # Check stock availability
        if quantity > product.stock:
            messages.error(request, f'Only {product.stock} items available in stock.')
            return redirect('products:product_detail', slug=slug)
        
        # Check if product already in cart
        cart_item, created = Cart.objects.get_or_create(
            user=request.user,
            product=product,
            defaults={'quantity': quantity}
        )
        
        if not created:
            # Update quantity if item already exists
            cart_item.quantity += quantity
            if cart_item.quantity > product.stock:
                cart_item.quantity = product.stock
                messages.warning(request, f'Maximum {product.stock} items allowed.')
            cart_item.save()
            messages.success(request, f'Updated {product.name} quantity in cart.')
        else:
            messages.success(request, f'Added {product.name} to cart.')
        
        return redirect('products:cart')
    
    return redirect('products:product_list')


@login_required
def update_cart(request, item_id):
    """Update cart item quantity"""
    if request.method == 'POST':
        cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
        quantity = int(request.POST.get('quantity', 1))
        
        if quantity > cart_item.product.stock:
            messages.error(request, f'Only {cart_item.product.stock} items available.')
            quantity = cart_item.product.stock
        
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, 'Cart updated successfully.')
        else:
            cart_item.delete()
            messages.success(request, 'Item removed from cart.')
    
    return redirect('products:cart')


@login_required
def remove_from_cart(request, item_id):
    """Remove item from cart"""
    if request.method == 'POST':
        cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
        product_name = cart_item.product.name
        cart_item.delete()
        messages.success(request, f'Removed {product_name} from cart.')
    
    return redirect('products:cart')


# Admin-only views for product management
from django.contrib.admin.views.decorators import staff_member_required
from .forms import ProductForm


@staff_member_required
def product_create(request):
    """Create new product (admin only)"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            messages.success(request, f'Product "{product.name}" created successfully!')
            return redirect('products:product_detail', slug=product.slug)
    else:
        form = ProductForm()
    
    context = {
        'form': form,
        'title': 'Create New Product',
        'button_text': 'Create Product'
    }
    return render(request, 'products/product_form.html', context)


@staff_member_required
def product_edit(request, slug):
    """Edit existing product (admin only)"""
    product = get_object_or_404(Product, slug=slug)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Product "{product.name}" updated successfully!')
            return redirect('products:product_detail', slug=product.slug)
    else:
        form = ProductForm(instance=product)
    
    context = {
        'form': form,
        'product': product,
        'title': f'Edit {product.name}',
        'button_text': 'Update Product'
    }
    return render(request, 'products/product_form.html', context)


@staff_member_required
def product_delete(request, slug):
    """Delete product (admin only)"""
    product = get_object_or_404(Product, slug=slug)
    
    if request.method == 'POST':
        product_name = product.name
        product.delete()
        messages.success(request, f'Product "{product_name}" deleted successfully!')
        return redirect('products:product_list')
    
    context = {
        'product': product,
    }
    return render(request, 'products/product_confirm_delete.html', context)