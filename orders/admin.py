"""
Admin configuration for orders app
"""
from django.contrib import admin
from .models import Order, OrderItem, ShippingAddress


class OrderItemInline(admin.TabularInline):
    """Inline admin for order items"""
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'quantity', 'price', 'total_price']
    can_delete = False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Admin for Order model"""
    list_display = ['order_number', 'user', 'full_name', 'total_amount', 
                    'payment_status', 'created_at']
    list_filter = ['payment_status', 'created_at']
    search_fields = ['order_number', 'user__username', 'email', 'full_name']
    readonly_fields = ['order_number', 'created_at', 'updated_at', 'paid_at', 
                       'stripe_payment_intent', 'order_items_count']
    inlines = [OrderItemInline]
    ordering = ['-created_at']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Order Information', {
            'fields': ('order_number', 'user', 'payment_status', 
                      'total_amount', 'order_items_count')
        }),
        ('Customer Information', {
            'fields': ('full_name', 'email', 'phone')
        }),
        ('Shipping Address', {
            'fields': ('address_line_1', 'address_line_2', 'city', 'state', 
                      'postal_code', 'country')
        }),
        ('Payment Details', {
            'fields': ('stripe_payment_intent', 'paid_at'),
            'classes': ('collapse',)
        }),
        ('Notes', {
            'fields': ('customer_notes', 'admin_notes'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        """Disable manual order creation in admin"""
        return False


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """Admin for OrderItem model"""
    list_display = ['order', 'product', 'quantity', 'price', 'total_price']
    list_filter = ['order__created_at']
    search_fields = ['order__order_number', 'product__name']
    readonly_fields = ['total_price']
    
    def has_add_permission(self, request):
        """Disable manual order item creation"""
        return False


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    """Admin for ShippingAddress model"""
    list_display = ['user', 'full_name', 'city', 'state', 'is_default', 'created_at']
    list_filter = ['is_default', 'country', 'created_at']
    search_fields = ['user__username', 'full_name', 'city', 'postal_code']
    readonly_fields = ['created_at']
    ordering = ['user', '-is_default', '-created_at']