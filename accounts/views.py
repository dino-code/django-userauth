from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from accounts.forms import UserForm


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

@login_required
def home(request):
    return render(request, "accounts/home.html", {})