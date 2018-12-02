from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

def index(request, name=""):
    return HttpResponse(f"Hello, world")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect("/") # Return to home page
    else:
        form = UserCreationForm()
    return render(request, "users/signup.html",{'form': form} )