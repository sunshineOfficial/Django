from django.urls import path

from lyceum.about import views

urlpatterns = [
    path("", views.description)
]
