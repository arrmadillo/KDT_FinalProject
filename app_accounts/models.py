import os
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.CharField(max_length=255, unique=True)
    

class Accountbyplanet(models.Model):
    nickname = models.CharField(max_length=15, blank=False, null=False)
    profile_image  = ProcessedImageField(
        upload_to  = 'accounts/',
        processors = [ResizeToFill(128, 128)],
        format     = 'JPEG',
        options    = {'quality': 100},
        blank      = True,
        null       = True,
    )
    backgounrd_image = ProcessedImageField(
        upload_to  = 'accounts/',
        processors = [ResizeToFill(500, 100)],
        format     = 'JPEG',
        options    = {'quality': 100},
        blank      = True,
        null       = True,
    )
    followings = models.ManyToManyField('self',
                                        symmetrical=False,
                                        blank=True,
                                        related_name='followers')
    user     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='accountsbyplanet')
    planet   = models.ForeignKey('app_planets.Planet', on_delete=models.CASCADE)
    
    is_confirmed = models.BooleanField(default=False)

    # accountbyplanet 삭제시 image file 삭제
    def delete(self, *args, **kwargs):
        if self.profile_image:
            path = self.profile_image.path
            if os.path.isfile(path):
                os.remove(path)
        if self.backgounrd_image:
            path = self.backgounrd_image.path
            if os.path.isfile(path):
                os.remove(path)
        super().delete(*args, **kwargs)

    # 업로드 가능한 profile image formats
    def get_profile_image_formats(self):
        return [
            ('JPEG', 'JPEG'),
            ('PNG', 'PNG'),
            ('GIF', 'GIF'),
        ]
    
    # 업로드 가능한 background image formats
    def get_background_image_formats(self):
        return [
            ('JPEG', 'JPEG'),
            ('PNG', 'PNG'),
            ('GIF', 'GIF'),
        ]

