from django.contrib import admin

# Register your models here.
from erp.models import Employee, SystemArg, Company, Project, SalaryStandard, SalaryTemplate, Attendance

admin.site.register(Employee)
admin.site.register(SystemArg)
admin.site.register(Company)
admin.site.register(Project)
admin.site.register(SalaryTemplate)
admin.site.register(SalaryStandard)
admin.site.register(Attendance)

