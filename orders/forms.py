"""
Forms for orders app
"""
from django import forms
from .models import Order, ShippingAddress


class CheckoutForm(forms.ModelForm):
    """Form for checkout process"""
    
    class Meta:
        model = Order
        fields = [
            'full_name', 'email', 'phone',
            'address_line_1', 'address_line_2',
            'city', 'state', 'postal_code', 'country',
            'customer_notes'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John Doe'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'john@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+1 (555) 123-4567'}),
            'address_line_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '123 Main St'}),
            'address_line_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apt 4B (optional)'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'New York'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NY'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '10001'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'USA'}),
            'customer_notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Any special delivery instructions? (optional)'
            }),
        }
        labels = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'address_line_1': 'Address Line 1',
            'address_line_2': 'Address Line 2 (Optional)',
            'city': 'City',
            'state': 'State / Province',
            'postal_code': 'Postal / ZIP Code',
            'country': 'Country',
            'customer_notes': 'Order Notes (Optional)',
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        # Pre-fill with user data if available
        if user and user.is_authenticated:
            self.fields['full_name'].initial = user.get_full_name()
            self.fields['email'].initial = user.email
            if hasattr(user, 'profile'):
                self.fields['phone'].initial = user.profile.phone
            
            # Pre-fill with default shipping address if exists
            default_address = ShippingAddress.objects.filter(
                user=user,
                is_default=True
            ).first()
            
            if default_address:
                self.fields['full_name'].initial = default_address.full_name
                self.fields['phone'].initial = default_address.phone
                self.fields['address_line_1'].initial = default_address.address_line_1
                self.fields['address_line_2'].initial = default_address.address_line_2
                self.fields['city'].initial = default_address.city
                self.fields['state'].initial = default_address.state
                self.fields['postal_code'].initial = default_address.postal_code
                self.fields['country'].initial = default_address.country


class ShippingAddressForm(forms.ModelForm):
    """Form for saving shipping addresses"""
    
    class Meta:
        model = ShippingAddress
        fields = [
            'full_name', 'phone',
            'address_line_1', 'address_line_2',
            'city', 'state', 'postal_code', 'country',
            'is_default'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address_line_1': forms.TextInput(attrs={'class': 'form-control'}),
            'address_line_2': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'is_default': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }