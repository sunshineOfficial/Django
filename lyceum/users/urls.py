from django.urls import path, re_path
from users import views

urlpatterns = [
    re_path(r'^users/(?P<id>\d+)/$', views.user_detail),
    path('users/', views.user_list),
    path('signup/', views.signup),
    path('profile/', views.profile)
]