from django.contrib import admin
from general.models import *

# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_code', 'is_active')
admin.site.register(Country, CountryAdmin)
