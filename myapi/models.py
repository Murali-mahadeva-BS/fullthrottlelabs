from django.db import models


class Userinfo(models.Model):
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=100)


class ActivityPeriod(models.Model):
    activity_periods = models.ForeignKey(
        Userinfo, related_name="activity_periods", on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
