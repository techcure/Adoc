from django.conf import settings
from django.db import models
from django.utils import timezone
import tempfile

from django.core.files import File


class Reg(models.Model):
    name = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    upload = models.FileField(upload_to = 'static/files', blank=True, null=True) 
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email


class Files(models.Model):
    upload = models.FileField(upload_to = 'static/files', blank=True, null=True) 
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.upload