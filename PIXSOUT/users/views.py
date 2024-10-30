from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            user = authenticate(request, username=form_data['username'], password=form_data['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = LoginForm()
    data = {
        'form': form
    }
    return render(request, 'users/login.html', context=data)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
