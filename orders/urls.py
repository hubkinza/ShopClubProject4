"""
URL patterns for orders app
"""
from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    # Checkout
    path('checkout/', views.checkout, name='checkout'),
    path('create-payment-intent/', views.create_payment_intent, name='create_payment_intent'),
    
    # Orders
    path('success/<str:order_number>/', views.order_success, name='order_success'),
    path('my-orders/', views.order_list, name='order_list'),
    path('order/<str:order_number>/', views.order_detail, name='order_detail'),
    
    # Stripe Webhook
    path('webhook/', views.stripe_webhook, name='stripe_webhook'),
]