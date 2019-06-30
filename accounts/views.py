from django.shortcuts import render, redirect
from .forms import UserRegistration
from django.http import HttpResponse
from django.contrib import messages


def register(request):
    # Redirect logged in users
    if request.user.is_authenticated:
        return redirect('/accounts/profile')
    
    # First take care of the post req
    if request.method == 'POST':
        # Create a form and populate it with data from the req
        form = UserRegistration(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created!')
            return redirect('/accounts/login')
    else:
        # It's a get req so the form is empty
        form = UserRegistration()
    
    # Render the page
    return render(request, 'accounts/register.html', {'form': form})


def profile(request):
    return render(request, 'accounts/profile.html')



    


