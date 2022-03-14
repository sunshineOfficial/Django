from django.urls import path
from catalog import views

urlpatterns = [
    path('<int:id>/', views.item_detail),
    path('', views.item_list)
]