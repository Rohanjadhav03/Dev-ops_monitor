import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import os

SYSTEM_MONITOR_URL = os.environ.get('SYSTEM_MONITOR_URL', 'http://localhost:8000/api/stats/')
REPORT_SERVICE_URL = os.environ.get('REPORT_SERVICE_URL', 'http://localhost:8001/api/history/')

def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        from django.contrib.auth.models import User
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

@api_view(['GET'])
@login_required
def proxy_stats(request):
    try:
        response = requests.get(SYSTEM_MONITOR_URL)
        return Response(response.json())
    except requests.exceptions.RequestException:
        return Response({'error': 'Could not connect to system-monitor'}, status=503)

@api_view(['GET'])
@login_required
def proxy_history(request):
    try:
        response = requests.get(REPORT_SERVICE_URL)
        return Response(response.json())
    except requests.exceptions.RequestException:
        return Response({'error': 'Could not connect to report-service'}, status=503)