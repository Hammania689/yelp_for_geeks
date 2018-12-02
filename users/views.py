from django.http import HttpResponse
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request, name=""):
    return HttpResponse(f"Hello, world")

@login_required
def profile(request):
    user_form = UserUpdateForm()
    profile_form  = ProfileUpdateForm()


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