from django.shortcuts import render
from django.http import HttpResponse


def user_list(request):
    return HttpResponse('Список пользователей')


def user_detail(request, pk):
    return HttpResponse(f'Информация о пользователе {pk}')


def signup(request):
    return HttpResponse('Регистрация')


def profile(request):
    return HttpResponse('Мой профиль')
