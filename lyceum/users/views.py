from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Prefetch
from django.shortcuts import render, redirect

from rating.models import User, Rating
from .models import Profile


def user_list(request):
    template = 'users/user_list.html'
    user = User.objects.filter(username=request.user.username).first()
    users = User.objects.only('username')
    context = {
        'user': user,
        'users': users
    }
    return render(request, template, context)


def user_detail(request, pk):
    template = 'users/user_detail.html'
    user = User.objects.filter(username=request.user.username)
    d_user = User.objects.filter(pk=pk).only('email', 'first_name', 'last_name').select_related(
        'profile').prefetch_related(
        Prefetch('rating', queryset=Rating.objects.filter(star=5).only('item').select_related('item'))).first()
    context = {
        'pk': pk,
        'user': user,
        'd_user': d_user
    }
    return render(request, template, context)


def signup(request):
    template = 'users/signup.html'
    user = User.objects.filter(username=request.user.username).first()
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save()
        new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        login(request, new_user)
        return redirect('profile')
    context = {
        'user': user,
        'form': form
    }
    return render(request, template, context)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birthday']


@login_required
def profile(request):
    template = 'users/profile.html'
    user = User.objects.filter(username=request.user.username).only('email', 'first_name',
                                                                    'last_name').select_related(
        'profile').prefetch_related(
        Prefetch('rating', queryset=Rating.objects.filter(star=5).only('item').select_related('item'))).first()
    user_form = UserForm(request.POST or None)
    profile_form = ProfileForm(request.POST or None)
    if user_form.is_valid() and profile_form.is_valid():
        user.email = user_form.cleaned_data['email']
        user.username = user_form.cleaned_data['username']
        user.profile.birthday = profile_form.cleaned_data['birthday']
        user.save()
    context = {
        'user': user,
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, template, context)
