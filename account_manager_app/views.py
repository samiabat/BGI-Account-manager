from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth.hashers import make_password

from .models import Sector, Employee, SectorRole, Role, EmployeeSectorRole
from .serializers import EmployeeSectorRoleSerializer, SectorRoleSerializer, SectorSerializer, EmployeeSerializer, RoleSerializer


@csrf_exempt
@api_view (['GET', 'POST', 'DELETE', 'PUT'])
def sectorAPI(request, pk=-1):
    if request.method == "GET":
        if pk==-1:
            sectors = Sector.objects.all().order_by('-created_date')
            sectors_serializer = SectorSerializer(sectors, many=True)
            return JsonResponse(sectors_serializer.data, status = 200, safe=False)
        else:
            try:
                sector = Sector.objects.get(id=pk)
                if sector is not None:
                    sector_serializer = SectorSerializer(sector)
                    return JsonResponse(sector_serializer.data, status = 200,  safe=False)
            except:
                responce = {"message":"No Such Sector!"}
                return JsonResponse(responce, status = 404,  safe=False) 
        
    elif request.method == "POST":
        sector_data = JSONParser().parse(request)
        try :
            other_sector = Sector.objects.get(name = sector_data["name"])
            if other_sector:
                responce = {"message": "The Sector Name Already Exist!"}
                return JsonResponse(message, status = 400,  safe=False)
        except:
            sector_serializer = SectorSerializer(data=sector_data)
            if sector_serializer.is_valid():
                sector_serializer.save()
                message = {"message":"Sector Register Sucessfully!"}
                return JsonResponse(message, status=201, safe=False)
            message = {"message": "Failed To Register!"}
            return JsonResponse(message, status=400, safe=False)
    
    elif request.method == "PUT":
        sector_data = JSONParser().parse(request)
        try:
            sector = Sector.objects.get(id = pk)
            sector_serializer = SectorSerializer(sector, data=sector_data)
            if sector_serializer.is_valid():
                sector_serializer.save()
                responce = {"message":"Data Updated Sucessfully!"}
                return JsonResponse(message, status = 204, safe=False)
            message = {"message": "Unable To Update!"}
            return JsonResponse(message, status = 401, safe=False)
        except:
            message = {"message":"The Same ID Is Already In Use!"}
            return JsonResponse(message, status = 401, safe=False)
    elif request.method == "DELETE":
        try:
            sector = Sector.objects.get(id=pk)
            if sector:
                sector.delete()
                message = {"message": "Sector Deleted Sucessfully!"}
                return JsonResponse(message, status = 201,  safe=False)
        except:
            message = {"message": "No Such Sector!"}
            return JsonResponse(message, status = 404, safe=False)
        
@csrf_exempt
@api_view (['GET', 'POST', 'DELETE', 'PUT'])
def employeeAPI(request, pk=-1):
    if request.method == "GET":
        if pk==-1:
            employees = Employee.objects.all()
            employees_serializer = EmployeeSerializer(employees, many=True)
            return JsonResponse(employees_serializer.data, status = 200, safe=False)
        else:
            try:
                employee = Employee.objects.get(id=pk)
                if employee is not None:
                    employee_serializer = EmployeeSerializer(employee)
                    return JsonResponse(employee_serializer.data, status = 201, safe=False)
            except:
                responce = {"message":"No Such Employee!"}
                return JsonResponse(responce, status = 404,  safe=False) 
        
    elif request.method == "POST":
        employee_data = JSONParser().parse(request)
        try :
            other_employee = Employee.objects.get(username = employee_data["username"])
            if other_employee:
                responce = {"message": "The Employee Name Already Exist!"}
                return JsonResponse(message, status = 400,  safe=False)
        except:
            # employee_data['password'] = make_password(employee_data["password"])
            employee_serializer = EmployeeSerializer(data=employee_data)
            if employee_serializer.is_valid():
                employee_serializer.save()
                message = {"message":"Employee Registered Sucessfully!"}
                return JsonResponse(message, status=201, safe=False)
            message = {"message": "Failed To Register!"}
            return JsonResponse(message, status=400, safe=False)
    
    elif request.method == "PUT":
        employee_data = JSONParser().parse(request)
        employee = Employee.objects.get(id = pk)
        # employee_data['password'] = make_password(employee_data["password"])
        employee_serializer = EmployeeSerializer(employee, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            message = {"message":"Data Updated Sucessfully!"}
            return JsonResponse(message, status = 204, safe=False)
        message = {"message": "Unable To Update!"}
        return JsonResponse(message, status = 400, safe=False)
    elif request.method == "DELETE":
        try:
            employee = Employee.objects.get(id=pk)
            if employee:
                employee.delete()
                message = {"message": "Employee Deleted Sucessfully!"}
                return JsonResponse(message, status = 201,  safe=False)
        except:
            message = {"message": "No Such Employee!"}
            return JsonResponse(message, status = 404, safe=False)
@csrf_exempt
@api_view (['GET', 'POST', 'DELETE', 'PUT'])
def roleAPI(request, pk=-1):
    if request.method == "GET":
        if pk==-1:
            roles = Role.objects.all()
            roles_serializer = RoleSerializer(roles, many=True)
            return JsonResponse(roles_serializer.data, status = 200, safe=False)
        else:
            try:
                role = Role.objects.get(id=pk)
                if role is not None:
                    role_serializer = RoleSerializer(role)
                    return JsonResponse(role_serializer.data, status = 200, safe=False)
            except:
                responce = {"message":"No Such Role!"}
                return JsonResponse(responce, status = 404,  safe=False) 
        
    elif request.method == "POST":
        
        role_data = JSONParser().parse(request)
        try :
            other_role = Sector.objects.get(name = role_data["name"])
            if other_role:
                responce = {"message": "The Role Name Already Exist!"}
                return JsonResponse(message, status = 400,  safe=False)
        except:
            role_serializer = RoleSerializer(data=role_data)
            if role_serializer.is_valid():
                role_serializer.save()
                message = {"message":"Role Register Sucessfully!"}
                return JsonResponse(message, status=201, safe=False)
            message = {"message": "Failed To Register!"}
            return JsonResponse(message, status=400, safe=False)
    
    elif request.method == "PUT":
        role_data = JSONParser().parse(request)
        try:
            role = role.objects.get(id = pk)
            role_serializer = RoleSerializer(role, data=role_data)
            if role_serializer.is_valid():
                role_serializer.save()
                responce = {"message":"Data Updated Sucessfully!"}
                return JsonResponse(message, status = 204, safe=False)
            message = {"message": "Unable To Update!"}
            return JsonResponse(message, status = 401, safe=False)
        except:
            message = {"message":"The Same ID Is Already In Use!"}
            return JsonResponse(message, status = 401, safe=False)
    elif request.method == "DELETE":
        try:
            role = Role.objects.get(id=pk)
            if role:
                role.delete()
                message = {"message": "Role Deleted Sucessfully!"}
                return JsonResponse(message, status = 201,  safe=False)
        except:
            message = {"message": "No Such Role!"}
            return JsonResponse(message, status = 404, safe=False)
        
@csrf_exempt
@api_view (['GET', 'POST', 'DELETE', 'PUT'])
def sectorRoleAPI(request, pk=-1):
    if request.method == "GET":
        if pk==-1:
            sectorRoles = SectorRole.objects.all()
            sector_role_serializer = SectorRoleSerializer(sectorRoles, many=True)
            return JsonResponse(sector_role_serializer.data, status = 200, safe=False)
        else:
            try:
                sector_role = SectorRole.objects.get(id=pk)
                if sector_role is not None:
                    sector_role_serializer = SectorRole(sector_role)
                    return JsonResponse(sector_role_serializer.data, status = 200, safe=False)
            except:
                responce = {"message":"No Such employee sector!"}
                return JsonResponse(responce, status = 404,  safe=False) 
        
    elif request.method == "POST":
        sector_role_data = JSONParser().parse(request)
        try :
            other_sector_role_data = SectorRole.objects.get(name = sector_role_data["name"])
            if other_sector_role_data:
                responce = {"message": "The employee_sector Name Already Exist!"}
                return JsonResponse(message, status = 400,  safe=False)
        except:
            sector_role_serializer = SectorRole(data=sector_role_data)
            if sector_role_serializer.is_valid():
                sector_role_serializer.save()
                message = {"message":"employee_sector Register Sucessfully!"}
                return JsonResponse(message, status=201, safe=False)
            message = {"message": "Failed To Register!"}
            return JsonResponse(message, status=400, safe=False)
    
    elif request.method == "PUT":
        sector_role_data = JSONParser().parse(request)
        try:
            sector_role = SectorRole.objects.get(id = pk)
            sector_role_serializer = SectorRole(sector_role, data=sector_role_data)
            if sector_role_serializer.is_valid():
                sector_role_serializer.save()
                responce = {"message":"Data Updated Sucessfully!"}
                return JsonResponse(message, status = 204, safe=False)
            message = {"message": "Unable To Update!"}
            return JsonResponse(message, status = 401, safe=False)
        except:
            message = {"message":"The Same ID Is Already In Use!"}
            return JsonResponse(message, status = 401, safe=False)
    elif request.method == "DELETE":
        try:
            sector_role = SectorRole.objects.get(id=pk)
            if sector_role:
                sector_role.delete()
                message = {"message": "Role Deleted Sucessfully!"}
                return JsonResponse(message, status = 201,  safe=False)
        except:
            message = {"message": "No Such Role!"}
            return JsonResponse(message, status = 404, safe=False)


        
@csrf_exempt
@api_view (['GET', 'POST', 'DELETE', 'PUT'])
def employeeSectorRoleAPI(request, pk=-1):
    if request.method == "GET":
        if pk==-1:
            employee_sector_roles = EmployeeSectorRole.objects.all()
            employee_sector_role_serializer = EmployeeSectorRoleSerializer(employee_sector_roles, many=True)
            return JsonResponse(employee_sector_role_serializer.data, status = 200, safe=False)
        else:
            try:
                employee_sector_role = EmployeeSectorRole.objects.get(id=pk)
                if employee_sector_role is not None:
                    employee_sector_role_serializer = EmployeeSectorRole(employee_sector_role)
                    return JsonResponse(employee_sector_role_serializer.data, status = 200, safe=False)
            except:
                responce = {"message":"No Such employee sector!"}
                return JsonResponse(responce, status = 404,  safe=False) 
        
    elif request.method == "POST":
        employee_sector_role = JSONParser().parse(request)
        try :
            other_employee_sector_role = EmployeeSectorRole.objects.get(name = employee_sector_role["name"])
            if other_employee_sector_role:
                responce = {"message": "The employee_sector Name Already Exist!"}
                return JsonResponse(message, status = 400,  safe=False)
        except:
            employee_sector_role_serializer = EmployeeSectorRole(data=employee_sector_role)
            if employee_sector_role_serializer.is_valid():
                employee_sector_role_serializer.save()
                message = {"message":"employee_sector Register Sucessfully!"}
                return JsonResponse(message, status=201, safe=False)
            message = {"message": "Failed To Register!"}
            return JsonResponse(message, status=400, safe=False)
    
    elif request.method == "PUT":
        employee_sector_role_data = JSONParser().parse(request)
        try:
            employee_sector_role = EmployeeSectorRole.objects.get(id = pk)
            employee_sector_role_serializer = SectorRole(employee_sector_role, data=employee_sector_role_data)
            if employee_sector_role_serializer.is_valid():
                employee_sector_role_serializer.save()
                responce = {"message":"Data Updated Sucessfully!"}
                return JsonResponse(message, status = 204, safe=False)
            message = {"message": "Unable To Update!"}
            return JsonResponse(message, status = 401, safe=False)
        except:
            message = {"message":"The Same ID Is Already In Use!"}
            return JsonResponse(message, status = 401, safe=False)
    elif request.method == "DELETE":
        try:
            sector_role = SectorRole.objects.get(id=pk)
            if sector_role:
                sector_role.delete()
                message = {"message": "Role Deleted Sucessfully!"}
                return JsonResponse(message, status = 201,  safe=False)
        except:
            message = {"message": "No Such Role!"}
            return JsonResponse(message, status = 404, safe=False)


@csrf_exempt
@api_view (['GET'])
def stasticsAPI():
    emplyee = Employee.objects.count()
    sector = Sector.objects.count()
    role = Role.objects.count()
    stat = {"emplyee":emplyee, "sector": sector, "role": role}
    return JsonResponse(stat, statuscode = 200, safe=False)