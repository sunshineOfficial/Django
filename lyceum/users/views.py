from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.shortcuts import render, redirect

from rating.models import User, Rating
from .forms import UserForm, ProfileForm, BeautifulUserCreationForm


def user_list(request):
    template = 'users/user_list.html'
    users = User.objects.only('username')
    context = {
        'user': request.user,
        'users': users
    }
    return render(request, template, context)


def user_detail(request, pk):
    template = 'users/user_detail.html'
    detailed_user = User.objects.filter(pk=pk).only('email', 'first_name', 'last_name').select_related(
        'profile').prefetch_related(
        Prefetch('rating', queryset=Rating.objects.filter(star=5).only('item').select_related('item'))).first()
    context = {
        'pk': pk,
        'user': request.user,
        'detailed_user': detailed_user
    }
    return render(request, template, context)


def signup(request):
    template = 'users/signup.html'
    form = BeautifulUserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user, backend='users.backends.EmailBackend')
        return redirect('profile')
    context = {
        'user': request.user,
        'form': form
    }
    return render(request, template, context)


@login_required
def profile(request):
    template = 'users/profile.html'
    user = User.objects.filter(username=request.user.username).only('email', 'first_name',
                                                                    'last_name').select_related(
        'profile').prefetch_related(
        Prefetch('rating', queryset=Rating.objects.filter(star=5).only('item').select_related('item'))).first()
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    context = {
        'user': user,
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, template, context)
