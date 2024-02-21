from django.contrib.auth import logout, authenticate, login
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'


class CustomLoginView(View):
    template_name = 'accounts/login.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=str(password))

        if user:
            login(request, user)
            return redirect('home')
        else:
            context = {'error_message': 'Invalid username or password'}
            return render(request, self.template_name, context)


class CustomLogoutView(TemplateView):
    template_name = "accounts/logout.html"

    def get(self, request: HttpRequest):
        logout(request)
        return render(request, self.template_name)
