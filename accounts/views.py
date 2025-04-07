from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from accounts.forms import UserForm, UserUpdateForm


# Create your views here.
def login(request):
    # Form has been submitted.
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect(reverse("accounts:home"))
    # If it's a GET request, return an empty form
    else:
        form = AuthenticationForm()

    return render(request, "accounts/login.html", {"form": form})

def register(request):
    # Form has been submitted.
    if request.method == "POST":
        # bind data to form
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("accounts:login"))
    # If it's a GET request, return an empty form
    else:
        form = UserForm()

    return render(request, "accounts/register.html", {"form": form})

def logout(request):
    auth_logout(request)
    return redirect("accounts:login")

@login_required
def home(request):
    return render(request, "accounts/home.html", {})

@login_required
def profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, "accounts/profile.html", {"form": form})