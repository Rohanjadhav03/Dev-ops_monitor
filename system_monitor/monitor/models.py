from django.db import models

class SystemStat(models.Model):
    cpu_usage_percent = models.FloatField()
    ram_usage_percent = models.FloatField()
    disk_usage_percent = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CPU: {self.cpu_usage_percent}%, RAM: {self.ram_usage_percent}%, Disk: {self.disk_usage_percent}%"