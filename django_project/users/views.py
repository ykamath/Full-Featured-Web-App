from django.shortcuts import render, redirect # Redirects user to another URL
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Decorator checks if user is logged in before visiting a page (i.e. profile)
from .forms import UserRegisterForm

def register(request):
    # Use built-in form, to make it easier for user registration
    # Create form here for templates
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # Filter username in a variable
            messages.success(request, f'Account created for {username}! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    # Form to create new User
    return render(request, 'users/register.html', {'form': form})
# Decorator
@login_required
def profile(request):
    # Need to check if user has been logged in before looking at this page
    return render(request, 'users/profile.html')
