from django.shortcuts import render

# Create your views here.
"""
Views for accounts app
"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .models import UserProfile


@login_required
def profile(request):
    """User profile page"""
    user = request.user
    profile = user.profile
    
    if request.method == 'POST':
        # Handle profile update
        if 'update_profile' in request.POST:
            user.first_name = request.POST.get('first_name', '')
            user.last_name = request.POST.get('last_name', '')
            user.save()
            
            profile.phone = request.POST.get('phone', '')
            profile.bio = request.POST.get('bio', '')
            profile.newsletter_subscription = 'newsletter_subscription' in request.POST
            profile.sms_notifications = 'sms_notifications' in request.POST
            
            # Handle avatar upload
            if request.FILES.get('avatar'):
                profile.avatar = request.FILES['avatar']
            
            profile.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('accounts:profile')
        
        # Handle password change
        elif 'change_password' in request.POST:
            password_form = PasswordChangeForm(user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Password changed successfully!')
                return redirect('accounts:profile')
            else:
                for error in password_form.errors.values():
                    messages.error(request, error)
    
    context = {
        'user': user,
        'profile': profile,
    }
    return render(request, 'account/profile.html', context)