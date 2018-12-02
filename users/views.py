from django.http import HttpResponse
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request, name=""):
    return HttpResponse(f"Hello, world")


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f"Your Account has been updated")
            return redirect("profile")  # Return to home page

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'users/profile.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your Account has been created! You are now able to login!")
            return redirect("login") # Return to home page
        messages.error(request, _('Please correct the error below.'))
    else:
        form = UserRegisterForm()
    return render(request, "users/signup.html", {'form': form})