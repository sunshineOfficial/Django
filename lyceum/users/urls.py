from django.urls import path

from users import views

urlpatterns = [
    path('users/<int:pk>/', views.user_detail),
    path('users/', views.user_list, name='user_list'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile')
]
