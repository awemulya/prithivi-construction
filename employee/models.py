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
    phone = models.CharField(max_length=10)
    marital_status = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    date_of_birth = models.DateField(null=True)
    date_joined = models.DateField(null=True)
    site = models.ForeignKey(Project, default=DEFAULT_PROJECT_ID, related_name="employee")

    def age(self):
        if not self.date_of_birth:
            return None
        return int((datetime.date.today() - self.date_of_birth).days / 365.25)

    def __unicode__(self):
        return '{0} ->  {1}'.format(self.name, self.role.role)


class Salary(models.Model):
    employee = models.ForeignKey(Employee, related_name="salary")
    salary = models.FloatField(default=0.0)
    date = models.DateField(default=datetime.date.today)

    def __unicode__(self):
        return '{0} -> {1}'.format(self.employee.name, self.salary)


class Payment(models.Model):
    employee = models.ForeignKey(Employee, related_name="payment")
    absent_days = models.IntegerField(default=0)
    date = models.DateField(default=datetime.date.today)
    year = models.IntegerField()
    month = models.CharField(max_length=2)

    def current_salary(self):
        return self.employee.salary.all().filter(date__lt=self.date).order_by('-date')[0].salary if self.employee.salary.all() else 0

    def amount(self):
        salary = self.current_salary()
        return salary-(salary*(self.absent_days))/30

    def __unicode__(self):
        return '{0} -> {1}'.format(self.employee.name, self.amount())


class SalaryVoucher(models.Model):
    voucher_no = models.PositiveIntegerField(blank=True, null=True)
    date = models.DateField(default=datetime.datetime.today)


class SalaryVoucherRow(models.Model):
    sn = models.PositiveIntegerField()
    employee = models.ForeignKey(Employee)
    paid_date = models.DateField(default=datetime.datetime.today)
    amount = models.FloatField()
    start_date = models.DateField()
    last_date = models.DateField()
    salary_voucher = models.ForeignKey(SalaryVoucher, related_name='rows')
