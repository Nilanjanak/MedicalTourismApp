from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .forms import LoginForm, UserRegistrationForm


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password using set_password to hash it
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object to the database
            new_user.save()
            # Render the registration done template
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        # If GET request, display an empty form
        user_form = UserRegistrationForm()
    
    return render(request, 'registration/signup.html', {'user_form': user_form})
