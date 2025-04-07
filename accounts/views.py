from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from accounts.forms import UserForm


# Create your views here.
def login(request):
    # Form has been submitted.
    if request.method == "post":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("")
    # If it's a GET request, return an empty form
    else:
        form = AuthenticationForm()

    return render(request, "accounts/login.html", {"form": form})

def register(request):
    # Form has been submitted.
    if request.method == "post":
        # bind data to form
        form = UserForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse("login/"))
    # If it's a GET request, return an empty form
    else:
        form = UserForm()

    return render(request, "accounts/register.html", {"form": form})