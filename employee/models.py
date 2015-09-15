import datetime
from django.db import models
from project.models import Project
DEFAULT_PROJECT_ID = 2


class EmployeeRole(models.Model):
    role = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def __unicode__(self):
        return '{0}'.format(self.role)


class Employee(models.Model):
    role = models.ForeignKey(EmployeeRole)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    sex = models.CharField(max_length=20)
    marital_status = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True)
    date_joined = models.DateField(null=True)
    site = models.ForeignKey(Project, default=DEFAULT_PROJECT_ID, related_name="employee")

    def age(self):
        if not self.date_of_birth:
            return None
        return int((datetime.date.today() - self.date_of_birth).days / 365.25)

    def __unicode__(self):
        return '{0} ->  {1}'.format(self.name, self.role.role)