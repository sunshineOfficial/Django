from django.urls import path

from users import views

urlpatterns = [
    path('users/<int:pk>/', views.user_detail),
    path('users/', views.user_list),
    path('signup/', views.signup),
    path('profile/', views.profile)
]
