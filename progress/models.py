import datetime
from django.utils.translation import ugettext as _
from django.db import models
from project.models import Project


class Task(models.Model):
    description = models.CharField(max_length=254)
    status_choices = [('planning', _('Planning')), ('pending', _('Pending')), ('started', _('Started')),
                      ('completed', _('Completed'))]
    progress_status = models.CharField(choices=status_choices, max_length=50, default="started")
    status = models.BooleanField(default=False)
    start_date = models.DateField(default=datetime.datetime.today)
    deadline = models.DateField(null=True, blank=True)
    site = models.ForeignKey(Project, related_name='task')


class Rows(models.Model):
    description = models.CharField(max_length=254)
    status_choices = [('planning', _('Planning')), ('pending', _('Pending')), ('started', _('Started')),
                      ('completed', _('Completed'))]
    progress_status = models.CharField(choices=status_choices, max_length=50, default="started")
    status = models.BooleanField(default=False)
    start_date = models.DateField(default=datetime.datetime.today)
    deadline = models.DateField(null=True, blank=True)
    task = models.ForeignKey(Task, related_name='rows')

