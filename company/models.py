from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50)
    pan = models.CharField(max_length=20)
    established = models.DateField(null=True)
    address = models.CharField(max_length=50)

    def __unicode__(self):
        return '{0}'.format(self.name)
