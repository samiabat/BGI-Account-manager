from rest_framework.serializers import ModelSerializer
from .models import Sector, Employee, Role, EmployeeSector, EmployeeRole

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class SectorSerializer(ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'

class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class EmployeeSectorSerializer(ModelSerializer):
    class Meta:
        model = EmployeeSector
        fields = '__all__'
class EmployeeRoleSerializer(ModelSerializer):
    class Meta:
        model = EmployeeRole
        fields = '__all__'