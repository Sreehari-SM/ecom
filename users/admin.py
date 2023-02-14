from django.contrib import admin
from users.models import *

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'is_verified')
    search_fields = ('name', 'phone')
admin.site.register(Profile, ProfileAdmin)


class OtpRecordAdmin(admin.ModelAdmin):
    list_display = ('phone', 'otp', 'attempts', 'is_applied')
    search_fields = ('phone', 'otp')
admin.site.register(OtpRecord, OtpRecordAdmin)