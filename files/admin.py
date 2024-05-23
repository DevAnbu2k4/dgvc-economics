from django.contrib import admin
from .models import subject, pdf
from .models import UserTracking
# Register your models here.
admin.site.register(subject)
admin.site.register(pdf)

@admin.register(UserTracking)
class UserTrackingAdmin(admin.ModelAdmin):
    list_display = ('user', 'ip_address', 'device', 'timestamp')
    list_filter = ('user', 'ip_address', 'device', 'timestamp')
    search_fields = ('user__username', 'ip_address', 'device')
