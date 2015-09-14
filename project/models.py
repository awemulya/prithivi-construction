from django.db import models
from user.models import AweUser


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    start_date = models.DateField(null=True)
    completion_date = models.DateField(null=True)
    incharge = models.ManyToManyField(AweUser)

    def __unicode__(self):
        return '{0}'.format(self.name)