from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserUpdateForm, UserProfileForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    # Render an empty form and if it's a post req render one with the data
    form = UserRegistrationForm()

    # Redirect logged in users
    if request.user.is_authenticated:
        messages.info(request, f'You are already logged in!')
        # 
        # Messages are stored in cookies and using redirect removes the cookie 
        # strange enough cuz down there works on form.is_valid()
        # 
        return render(request, 'accounts/profile.html')
    
    # First take care of the post req
    if request.method == 'POST':
        # Create a form and populate it with data from the req
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created!')
            return redirect('/accounts/login')
    
    # Render the page
    return render(request, 'accounts/register.html', locals())


def profile(request):
    return render(request, 'accounts/profile.html')

#TODO make value for form fields to be the initial data if form.is_valid fails
@login_required
def profile_update(request):
    # Render empty forms for get
    user_form = UserUpdateForm(instance=request.user)
    profile_form = UserProfileForm(instance=request.user.profile)

     # Take care of the POST req
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('profile')

    return render(request, 'accounts/profile_update.html', locals())

def error_404(request, exception):
    return render(request, 'accounts/error_404.html', status=404)



    


