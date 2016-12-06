import datetime
import pytz

from django.db import models


class UserManager(models.Manager):

    def in_recent_week(self):

        # get time gap utc - local
        time_gap = datetime.datetime.utcnow() - datetime.datetime.now()

        # custom time_now using instead of datetime.datetime.now(pytz.UTC)
        time_now = datetime.datetime(2016, 11, 17, 8, 11, 39, tzinfo=pytz.UTC)

        today_end = datetime.datetime.combine(time_now, datetime.time.max) - time_gap

        week_ago = today_end - datetime.timedelta(7)

        return self.exclude(created_at__lte=(week_ago)).order_by("created_at")


class User(models.Model):

    objects = UserManager()

    created_at = models.DateTimeField(auto_now_add=True)
    device = models.CharField(max_length=100)

    def __str__(self):
        query_info = "{id_no}/{created}/{device}".format(id_no=self.id, created=self.created_at, device=self.device)
        return query_info
