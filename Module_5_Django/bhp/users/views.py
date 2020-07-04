from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as logout_
from django.http import HttpResponseRedirect

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView

from users.forms import RegisterForm
from users.models import User

from django import views


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data.get('username'),
                email=form.cleaned_data.get('email'),
            )
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            login(request, user)
            return redirect('/')
    return render(request, 'users/register_page.html', {'form': form})


def logout(request):
    logout_(request)
    return redirect('/')
