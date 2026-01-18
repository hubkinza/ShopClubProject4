"""
Views for orders app
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import stripe
import json

from .models import Order, OrderItem
from .forms import CheckoutForm
from products.models import Cart


# Configure Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def checkout(request):
    """Checkout page with payment form"""
    # Get cart items
    cart_items = Cart.objects.filter(user=request.user).select_related('product')
    
    if not cart_items.exists():
        messages.warning(request, 'Your cart is empty.')
        return redirect('products:cart')
    
    # Check stock availability
    for item in cart_items:
        if item.quantity > item.product.stock:
            messages.error(
                request,
                f'{item.product.name} has only {item.product.stock} items in stock.'
            )
            return redirect('products:cart')
    
    # Calculate totals
    subtotal = sum(item.total_price for item in cart_items)
    total = subtotal  # No tax
    
    if request.method == 'POST':
        form = CheckoutForm(request.POST, user=request.user)
        
        if form.is_valid():
            # Get payment intent ID from form
            payment_intent_id = request.POST.get('payment_intent_id')
            
            if not payment_intent_id:
                messages.error(request, 'Payment failed. Please try again.')
                return redirect('orders:checkout')
            
            # Create order
            order = form.save(commit=False)
            order.user = request.user
            order.total_amount = total
            order.stripe_payment_intent = payment_intent_id
            order.payment_status = 'paid'
            order.paid_at = timezone.now()
            order.save()
            
            # Create order items
            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    price=cart_item.product.price
                )
                
                # Update product stock
                cart_item.product.stock -= cart_item.quantity
                cart_item.product.save()
            
            # Clear cart
            cart_items.delete()
            
            messages.success(request, 'Order placed successfully!')
            return redirect('orders:order_success', order_number=order.order_number)
    else:
        form = CheckoutForm(user=request.user)
    
    context = {
        'form': form,
        'cart_items': cart_items,
        'subtotal': subtotal,
        'total': total,
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
    }
    return render(request, 'orders/checkout.html', context)


@login_required
def create_payment_intent(request):
    """Create Stripe Payment Intent"""
    if request.method == 'POST':
        try:
            # Get cart items
            cart_items = Cart.objects.filter(user=request.user).select_related('product')
            
            if not cart_items.exists():
                return JsonResponse({'error': 'Cart is empty'}, status=400)
            
            # Calculate total
            subtotal = sum(item.total_price for item in cart_items)
            total = subtotal  # No tax
            
            # Convert to cents for Stripe
            amount = int(total * 100)
            
            # Create Payment Intent
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='usd',
                metadata={
                    'user_id': request.user.id,
                    'user_email': request.user.email,
                }
            )
            
            return JsonResponse({
                'client_secret': intent.client_secret
            })
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)


@login_required
def order_success(request, order_number):
    """Order confirmation page"""
    order = get_object_or_404(Order, order_number=order_number, user=request.user)
    
    context = {
        'order': order,
    }
    return render(request, 'orders/order_success.html', context)


@login_required
def order_list(request):
    """Display user's orders"""
    orders = Order.objects.filter(user=request.user).prefetch_related('items__product')
    
    # Pagination
    paginator = Paginator(orders, 10)
    page_number = request.GET.get('page')
    orders = paginator.get_page(page_number)
    
    context = {
        'orders': orders,
    }
    return render(request, 'orders/order_list.html', context)


@login_required
def order_detail(request, order_number):
    """Display single order details"""
    order = get_object_or_404(
        Order,
        order_number=order_number,
        user=request.user
    )
    
    context = {
        'order': order,
    }
    return render(request, 'orders/order_detail.html', context)


@csrf_exempt
def stripe_webhook(request):
    """Handle Stripe webhooks"""
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        return JsonResponse({'error': 'Invalid payload'}, status=400)
    except stripe.error.SignatureVerificationError:
        return JsonResponse({'error': 'Invalid signature'}, status=400)
    
    # Handle the event
    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        
        # Update order payment status
        try:
            order = Order.objects.get(stripe_payment_intent=payment_intent['id'])
            order.payment_status = 'paid'
            order.paid_at = timezone.now()
            order.save()
        except Order.DoesNotExist:
            pass
    
    elif event['type'] == 'payment_intent.payment_failed':
        payment_intent = event['data']['object']
        
        # Update order payment status
        try:
            order = Order.objects.get(stripe_payment_intent=payment_intent['id'])
            order.payment_status = 'failed'
            order.save()
        except Order.DoesNotExist:
            pass
    
    return JsonResponse({'status': 'success'})