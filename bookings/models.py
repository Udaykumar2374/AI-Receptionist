from django.db import models
from calls.models import Call

class Booking(models.Model):
    call = models.ForeignKey(Call, on_delete=models.CASCADE)
    start_ts = models.DateTimeField(null=True, blank=True)
    end_ts = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=32, default="pending")  # pending|confirmed|failed
    provider = models.CharField(max_length=32, default="demo")
    meta_json = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking({self.status}) for Call#{self.call_id}"
