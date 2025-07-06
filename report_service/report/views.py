import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import SystemStat
from .serializers import SystemStatSerializer
from django.shortcuts import redirect
import os

SYSTEM_MONITOR_URL = os.environ.get('SYSTEM_MONITOR_URL', 'http://localhost:8000/api/stats/')

@api_view(['GET'])
def history(request):
    stats = SystemStat.objects.all().order_by('-created_at')[:10]
    if stats.exists():
        serializer = SystemStatSerializer(stats, many=True)
        return Response(serializer.data)
    else:
        try:
            response = requests.get(SYSTEM_MONITOR_URL)
            if response.status_code == 200:
                data = response.json()
                stat = SystemStat.objects.create(
                    cpu_usage_percent=data['cpu_usage_percent'],
                    ram_usage_percent=data['ram_usage_percent'],
                    disk_usage_percent=data['disk_usage_percent']
                )
                serializer = SystemStatSerializer(stat)
                return Response(serializer.data)
            else:
                return Response({'error': 'Failed to fetch data from system-monitor'}, status=502)
        except requests.exceptions.RequestException:
            return Response({'error': 'Could not connect to system-monitor'}, status=503)

def home_redirect(request):
    return redirect('/api/history/')