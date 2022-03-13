from django.urls import path, re_path
from catalog import views

urlpatterns = [
    re_path(r'^(?P<id>\d+)/$', views.item_detail),
    path('', views.item_list)
]