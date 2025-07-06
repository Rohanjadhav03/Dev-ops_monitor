from django.urls import path
from .views import stats, home_redirect

urlpatterns = [
    path('stats/', stats, name='stats'),
    path('', home_redirect, name='home'),
]