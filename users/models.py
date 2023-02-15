from django.db import models
from general.models import BaseModel
import uuid

# Create your models here.
class Profile(BaseModel):
    name = models.CharField(max_length=128, blank=True, null=True)
    phone = models.CharField(max_length=128, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    username = models.CharField(max_length=128, blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)
    otp = models.PositiveIntegerField(blank=True, null=True)


    class Meta:
        db_table = 'users_profile'
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
        ordering = ('name',)

    def __str__(self):
        return self.name


class OtpRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(max_length=16)
    otp = models.PositiveIntegerField()
    attempts = models.PositiveIntegerField(default=1)
    is_applied = models.BooleanField(default=False)
    country = models.ForeignKey('general.Country', on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(db_index=True, auto_now_add=True)
    date_updated = models.DateTimeField(db_index=True, auto_now_add=True)

    class Meta:
        db_table = 'users_otp_record'
        verbose_name = 'Otp Record'
        verbose_name_plural = 'Otp Records'
        ordering = ('-date_added',)
        
    def __str__(self):
        return self.phone
