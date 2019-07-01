from django.shortcuts import render, redirect
from .forms import UserRegistration, UserUpdateForm, UserProfileForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
    # Take care of the POST req
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'accounts/profile.html', context)

@login_required
def update_profile(request):
     # Take care of the POST req
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'accounts/profile_update.html', context)



    


