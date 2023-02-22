from django.contrib import admin
from notifications.models import *

# Register your models here.

class NotificationMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category',)
    search_fields = ('title', 'category')
admin.site.register(NotificationMessage, NotificationMessageAdmin)


class UserNotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'notification_message',)
    search_fields = ('user_id', 'id')
admin.site.register(UserNotification, UserNotificationAdmin)
