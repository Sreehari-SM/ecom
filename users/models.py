from django.db import models
from general.models import BaseModel

# Create your models here.
class Profile(BaseModel):
    name = models.CharField(max_length=128, blank=True, null=True)
    phone = models.CharField(max_length=128, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    username = models.CharField(max_length=128, blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)


    class Meta:
        db_table = 'users_profile'
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
        ordering = ('name',)

    def __str__(self):
        return self.name
