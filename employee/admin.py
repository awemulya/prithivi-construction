from django.contrib import admin
from .models import SalaryVoucher, SalaryVoucherRow, Employee, EmployeeRole 
from project.models import Project


admin.site.register(SalaryVoucher)
admin.site.register(Employee)
admin.site.register(EmployeeRole)
admin.site.register(Project)
admin.site.register(SalaryVoucherRow)

# Register your models here.
