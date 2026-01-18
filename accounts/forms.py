"""
Forms for accounts app
"""
from django import forms
from orders.models import ShippingAddress


class CustomSignupForm(forms.Form):
    """Extended signup form with address fields"""
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    phone = forms.CharField(max_length=20, required=False)
    address_line_1 = forms.CharField(max_length=250, required=True)
    address_line_2 = forms.CharField(max_length=250, required=False)
    city = forms.CharField(max_length=100, required=True)
    state = forms.CharField(max_length=100, required=True)
    postal_code = forms.CharField(max_length=20, required=True)
    country = forms.CharField(max_length=100, required=True, initial='USA')

    def signup(self, request, user):
        """Called by allauth after user is created"""
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        
        if hasattr(user, 'profile'):
            user.profile.phone = self.cleaned_data.get('phone', '')
            user.profile.save()
        
        ShippingAddress.objects.create(
            user=user,
            full_name=f"{user.first_name} {user.last_name}",
            phone=self.cleaned_data.get('phone', ''),
            address_line_1=self.cleaned_data['address_line_1'],
            address_line_2=self.cleaned_data.get('address_line_2', ''),
            city=self.cleaned_data['city'],
            state=self.cleaned_data['state'],
            postal_code=self.cleaned_data['postal_code'],
            country=self.cleaned_data['country'],
            is_default=True
        )