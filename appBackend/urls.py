from unicodedata import name
from django.urls import path
from . import views

app_name = 'appBackend'

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('menu/', views.MenuView.as_view(),name='menu'),
]
