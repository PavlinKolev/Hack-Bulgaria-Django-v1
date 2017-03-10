import uuid
import datetime
from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=datetime.datetime.now, blank=True)
    # data_set ===============================================

    def __str__(self):
        return "{} - {}".format(self.name, self.created_at)

    def id_str(self):
        return str(self.id)


class Data(models.Model):
    key = models.CharField(max_length=100, null=True, blank=True)
    value = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User)
    # user = models.ForeignKey(User, related_name='data')
