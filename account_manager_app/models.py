from django.db import models
class Role(models.Model):
    status = {
        ("1", 1),
        ("0", 0)
    }
    name = models.CharField(max_length=50)
    deleted = models.CharField(choices=status, max_length=2, default="0")
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
class Sector(models.Model):
    status = {
        ("1", 1),
        ("0", 0)
    }
    name = models.CharField(max_length=50)
    deleted = models.CharField(choices=status, max_length=2, default= "0")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)

class Employee(models.Model):
    status = {
        ("1", 1),
        ("0", 0)
    }
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    deleted = models.CharField(choices=status, max_length=2, default="0")
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    
class EmployeeSector(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

class EmployeeRole(models.Model):
    role = models.ForeignKey(Sector, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

class DP(models.Model):
    pass
class AX(models.Model):
    pass

class FinalEmployee(models.Model):
    lagon_name = models.CharField(max_length=50, null=True, blank=True)
    full_name = models.CharField(max_length=50, null=True, blank=True)
    display_name = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    sam_account = models.CharField(max_length=50, null=True, blank=True)
    company = models.CharField(max_length=50, null=True, blank=True)

