from django.contrib import admin

from .models import Employee, EmployeeRole, EmployeeSector, Sector, Role

# Register your models here.
admin.site.register(Employee)
admin.site.register(Sector)
admin.site.register(Role)
admin.site.register(EmployeeSector)
admin.site.register(EmployeeRole)