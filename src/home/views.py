from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView, View
from django.contrib.auth.models import User

from .forms import UserForm


class HomeView(TemplateView):
    template_name = "home/landing.html"


class LoginView(View):

    template_name = "home/login.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home_app:home')
        context = {}
        return render(request, self.template_name, context)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('trashcan_app:can-list')
        return self.get(request)


class SignupView(View):
    
    template_name = "home/signup.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home_app:home')
        context = {
            'errors': kwargs.get('errors'),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']

            user = User.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
            )
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('trashcan_app:can-list')
        return self.get(request, errors=form.errors)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('home_app:home')
