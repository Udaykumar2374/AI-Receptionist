from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from calls import views as call_views

def health(_request):
    return HttpResponse("OK")

urlpatterns = [
    path("health/", health),
    path("admin/", admin.site.urls),

    # Twilio Voice webhooks:
    path("webhooks/twilio/voice/", call_views.twilio_voice),
    path("webhooks/twilio/gather-action/", call_views.twilio_gather_action),

    # (Optional) Retell-like JSON webhook for testing without voice:
    path("webhooks/retell/events/", call_views.retell_events),
]
