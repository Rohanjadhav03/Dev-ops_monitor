from django.urls import path
from .views import history
from . import views
urlpatterns = [
    path('history/', history, name='history'),
    path('', views.home_redirect, name='home'),
]