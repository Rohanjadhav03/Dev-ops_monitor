from django.urls import path
from .views import stats
from . import views

urlpatterns = [
    path('stats/', stats, name='stats'),
    path('', views.home_redirect, name='home'),
]