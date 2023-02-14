from django.contrib import admin
from users.models import *

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'is_verified')
admin.site.register(Profile, ProfileAdmin)