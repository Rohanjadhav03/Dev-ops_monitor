import psutil
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SystemStat
from .serializers import SystemStatSerializer
from django.shortcuts import redirect

@api_view(['GET'])
def stats(request):
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    # Save to DB
    stat = SystemStat.objects.create(
        cpu_usage_percent=cpu,
        ram_usage_percent=ram,
        disk_usage_percent=disk
    )

    serializer = SystemStatSerializer(stat)
    return Response(serializer.data)

def home_redirect(request):
    return redirect('/api/stats/')