from django.http import HttpResponse
from .forms import UserRegisterForm
from django.shortcuts import render, redirect
from django.contrib import messages

def index(request, name=""):
    return HttpResponse(f"Hello, world")

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your Account has been created! You are now able to login!")
            return redirect("login") # Return to home page
    else:
        form = UserRegisterForm()
    return render(request, "users/signup.html", {'form': form})