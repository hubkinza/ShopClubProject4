"""
Forms for products app
"""
from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """Form for creating and editing products"""
    
    class Meta:
        model = Product
        fields = ['name', 'slug', 'category', 'description', 'price', 'stock', 'image', 'available']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Product Name'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'product-slug (auto-generated from name)'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Product description...'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'available': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        help_texts = {
            'slug': 'URL-friendly version of the name. Leave blank to auto-generate.',
            'price': 'Price in GBP',
            'stock': 'Number of items available',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make slug optional - it will be auto-generated from name if empty
        self.fields['slug'].required = False
    
    def clean_slug(self):
        """Auto-generate slug from name if not provided"""
        slug = self.cleaned_data.get('slug')
        name = self.cleaned_data.get('name')
        
        if not slug and name:
            from django.utils.text import slugify
            slug = slugify(name)
            
            # Ensure uniqueness
            original_slug = slug
            counter = 1
            while Product.objects.filter(slug=slug).exclude(pk=self.instance.pk).exists():
                slug = f"{original_slug}-{counter}"
                counter += 1
        
        return slug