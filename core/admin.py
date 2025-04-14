from django.contrib import admin
from .models import VisitLog

@admin.register(VisitLog)
class VisitLogAdmin(admin.ModelAdmin):
    list_display = ("page", "ip_address", "timestamp")
    list_filter = ("page",)
    search_fields = ("ip_address", "user_agent", "page")
