from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import LoginForm
from django.contrib.auth import logout


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse('home')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
