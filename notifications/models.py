from django.db import models
from general.models import BaseModel

# Create your models here.
NOTIFICATION_CATEGORY = (
    ('general', 'General'),
)

NOTIFICATION_STATUSES = (
    ('pending', 'Pending'),
    ('delivered', 'Delivered'),
    ('received', 'Received'),
)


class NotificationMessage(BaseModel):
    title = models.CharField(max_length=258, null=True, blank=True)
    Descryption = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=128, choices=NOTIFICATION_CATEGORY)

    class Meta:
        db_table = 'notifications_notification_message'
        verbose_name = 'notification message'
        verbose_name_plural = 'notification messages'
        ordering = ('title',)

    def __str__(self):
        return self.title


class UserNotification(BaseModel):
    user_id = models.CharField(max_length=128)
    notification_message = models.ForeignKey('notifications.NotificationMessage', on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=128, choices=NOTIFICATION_STATUSES, default='pending')

    class Meta:
        db_table = 'notifications_user_notification'
        verbose_name = 'user notification'
        verbose_name_plural = 'user notifications'
        ordering = ('date_added',)

    def __str__(self):
        return self.user_id
