from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomPasswordChangeForm
from dinings.models import Dining

# Create your views here.


def index(request):
    return render(request, 'accounts/index.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('dinings:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('dinings:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('dinings:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('dinings:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('dinings:index')


@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('dinings:index')


@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(
            request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dinings:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('dinings:index')
    else:
        form = CustomPasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)


def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    dinings = Dining.objects.order_by('-pk')
    context = {
        'person': person,
        'dinings': dinings,
    }
    return render(request, 'accounts/profile.html', context)


def follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)

    if request.user in person.followers.all():
        person.followers.remove(request.user)
    else:
        person.followers.add(request.user)
    return redirect('accounts:profile', person.username)
