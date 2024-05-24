from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class pdf(models.Model):
    name = models.CharField(max_length=100)
    text = models.FileField(upload_to='pdfs/')

class subject(models.Model):
    sub_name = models.CharField(max_length=100)
    sem = models.IntegerField()
    files = models.ManyToManyField(pdf)

    def __str__(self):
        return self.sub_name

class UserTracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ip_address = models.GenericIPAddressField()
    device = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.ip_address} - {self.device} - {self.timestamp}"
