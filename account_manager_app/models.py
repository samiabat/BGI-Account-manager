from statistics import mode
from django.db import models

class Sector(models.Model):
    stat = {
        ("Yes", True),
        ("No", False)
    }
    name = models.CharField(max_length=50)
    active = models.CharField(choices=stat, max_length=5, default=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
class Role(models.Model):
    stat = {
        ("Yes", True),
        ("No", False)
    }
    name = models.CharField(max_length=50)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    description = models.CharField(max_length=500, blank=True, null=True)
    active = models.CharField(choices=stat, max_length=5, default=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)


class Employee(models.Model):
    stat = {
        ("Yes", True),
        ("No", False)
    }
    full_name = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    sam_account = models.CharField(max_length=50, null=True, blank=True)
    company = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    department = models.CharField(max_length=50, null=True, blank=True)
    email_address = models.CharField(max_length=50, null=True, blank=True)
    telephone_number = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.CharField(max_length=50, null=True, blank=True)
    street_address = models.CharField(max_length=50, null=True, blank=True)
    login = models.CharField(max_length=50, null=True, blank=True)
    active = models.CharField(choices=stat, max_length=5, default=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)


class EmployeeSector(models.Model):
    sector_id = models.ForeignKey(Sector, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
