from django.urls import path
from .views import history, home_redirect

urlpatterns = [
    path('history/', history, name='history'),
    path('', home_redirect, name='home'),
]