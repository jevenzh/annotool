from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout



# Create your views here.
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class LoginView(generic.CreateView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('task_dispatch')
    template_name = 'registration/login.html'




def login(request):
    if not request.user.is_authenticated:
        return render(request, 'myapp/login_error.html')