from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path

from users import views
from .forms import BeautifulPasswordChangeForm, BeautifulAuthenticationForm, BeautifulSetPasswordForm, \
    BeautifulPasswordResetForm

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html', form_class=BeautifulAuthenticationForm),
         name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password_change/',
         PasswordChangeView.as_view(template_name='users/password_change.html', form_class=BeautifulPasswordChangeForm),
         name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
         name='password_change_done'),
    path('password_reset/',
         PasswordResetView.as_view(template_name='users/password_reset.html', form_class=BeautifulPasswordResetForm),
         name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html',
                                                                     form_class=BeautifulSetPasswordForm),
         name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('users/<int:pk>/', views.user_detail, name='user_detail'),
    path('users/', views.user_list, name='user_list'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile')
]
