from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id","call","status","start_ts","end_ts","provider","created_at")
    list_filter = ("status","provider")
