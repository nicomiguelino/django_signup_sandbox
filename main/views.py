from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, 'main/index.html')


class SignupView(View):
    def get(self, request):
        form = UserCreationForm(label_suffix='')
        return render(request, 'main/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('main:index')
