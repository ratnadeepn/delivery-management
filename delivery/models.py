from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class DeliveryTask(models.Model):
    title = models.CharField(max_length=200)
    priority = models.CharField(default="low", max_length=6)
    creation_date = models.DateTimeField(default=datetime.now, blank=True)
    created_by = models.CharField(max_length=200)
    status = models.CharField(default="new", max_length=9)
    is_available = models.BooleanField(default=True)
    is_accepted_by = models.CharField(default=None, max_length=200, null=True)
    is_declined_by =models.CharField(default="-1",max_length=200)
    is_priority =models.IntegerField(default=1)
    transition =models.CharField(default="new", max_length=1000)

    def get_absolute_url(self):
        return reverse('task_list')






