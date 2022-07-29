from rest_framework.serializers import ModelSerializer
from .models import *

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

class SectorRoleSerializer(ModelSerializer):
    class Meta:
        model = SectorRole
        fields = '__all__'
class EmployeeSectorRoleSerializer(ModelSerializer):
    class Meta:
        model = EmployeeSectorRole
        fields = '__all__'