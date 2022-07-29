from django.contrib import admin

from .models import Employee, EmployeeSectorRole, Sector, Role, SectorRole

# Register your models here.
admin.site.register(Employee)
admin.site.register(Sector)
admin.site.register(Role)
admin.site.register(SectorRole)
admin.site.register(EmployeeSectorRole)