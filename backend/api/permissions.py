from api.models import Employee
from rest_framework.permissions import BasePermission

class HasAccess(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        id = request.data.get('employee_id')
        emp = Employee.objects.get(id=id)
        if user.id == emp.user.id:
            return True
        if emp.auth_emp1 is not None:
            if user.id == emp.auth_emp1.id:
                return True
        if emp.auth_emp2 is not None:
            if user.id == emp.auth_emp2.id:
                return True
        return False
        
 