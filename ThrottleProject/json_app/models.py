from django.db import models
from django.contrib.postgres.fields import JSONField
# Create your models here.
class Members(models.Model):
    random_id = models.CharField(max_length = 50)
    real_name = models.CharField(max_length = 50)
    tz = models.TextField(default="")
    activity_periods = JSONField(default=list, null=True, blank=True)