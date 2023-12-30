from django.contrib import admin

from utils.admin import AuditableAdmin

from .models import Video

@admin.register(Video)
class VideoAdmin(AuditableAdmin):
    pass