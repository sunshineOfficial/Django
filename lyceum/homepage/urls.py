from django.urls import path, re_path
from homepage import views

urlpatterns = [
    path('', views.home)
]