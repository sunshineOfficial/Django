from django.urls import path, re_path
from about import views

urlpatterns = [
    path('', views.description)
]