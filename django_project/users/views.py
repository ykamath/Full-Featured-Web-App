from django.shortcuts import render, redirect # Redirects user to another URL
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    # Use built-in form, to make it easier for user registration
    # Create form here for templates
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # Filter username in a variable
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    # Form to create new User
    return render(request, 'users/register.html', {'form': form})
