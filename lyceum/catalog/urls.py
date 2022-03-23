from catalog import views
from django.urls import path

urlpatterns = [
    path("<int:pk>/", views.item_detail),
    path("", views.item_list)
]
