from django.db import models
from django.utils import timezone

# from django.core.files import File


class Reg(models.Model):
    name = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    upload = models.FileField(upload_to = 'static/files', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email


class Fill(models.Model):
    upload = models.FileField(upload_to='static/files', blank=True, null=True)


class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline


class Json(models.Model):
    data = models.JSONField(max_length=25, blank=True, null=True)
