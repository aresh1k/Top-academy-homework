from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import Art
from django.contrib.auth.decorators import login_required


def main(request):
    arts = Art.objects.all()
    return render(request, 'arts/home.html', {'arts': arts})


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'arts/register.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('')
            except IntegrityError:
                return render(request, 'arts/register.html', {'form': UserCreationForm(), 'error': 'Такое имя пользователя уже существует. Задайте другое'})
        else:
            return render(request, 'arts/register.html', {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})


@login_required
def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('main')


def loginuser(request):
    if request.method == "GET":
        return render(request, 'arts/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'arts/login.html', {'form': AuthenticationForm(), 'error': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('main')


def for_logged_users(request):
    return render(request, 'arts/for_signed_users.html')


@login_required
def for_logged_users_2(request):
    return render(request, 'arts/login_required.html')
