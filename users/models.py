from django.db import models
from django.contrib.auth.models import User, Group
from general.models import BaseModel
import uuid

from api.v1.general.functions import get_auto_id

# Create your models here.

PROFILE_TYPES = (
    ('product_manager', 'Product Manager'),
)


class Profile(BaseModel):
    name = models.CharField(max_length=128, blank=True, null=True)
    user = models.OneToOneField("auth.User",on_delete=models.CASCADE, blank=True, null=True)
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


class ChiefProfile(BaseModel):
    name = models.CharField(max_length=128)
    user = models.OneToOneField("auth.User",on_delete=models.CASCADE, blank=True, null=True)
    user_name = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    email = models.EmailField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    profile_type = models.CharField(max_length=128, choices=PROFILE_TYPES, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.creator:

            if self._state.adding:
                auto_id = get_auto_id(ChiefProfile)

                chief_username = self.username
                if self.password:
                    password = decrypt(self.password)
                else:
                    password = User.objects.make_random_password(length=12, allowed_chars="abcdefghjkmnpqrstuvwzyx#@*%$ABCDEFGHJKLMNPQRSTUVWXYZ23456789")
                
                chief_email = f"{chief_username}@talrop.com"

                user = User.objects.create_user(
                    username=chief_username,
                    email=chief_email,
                    password=password
                )
                
                if self.profile_type == "product_manager":
                    pa_engineer_group, created = Group.objects.get_or_create(name='product_manager')
                    pa_engineer_group.user_set.add(user)
                self.auto_id = auto_id
                self.user = user
                self.password = encrypt(password)

        super(ChiefProfile, self).save(*args, **kwargs)

    class Meta:
        db_table = 'users_chief_profile'
        verbose_name = 'Chief Profile'
        verbose_name_plural = 'Chief Profiles'
        ordering = ('-date_added',)
        
    def __str__(self):
        return self.name
