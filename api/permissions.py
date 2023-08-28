from rest_framework import permissions

# class AdminOrReadOnly(permissions.IsAdminUser):

#     def has_permission(self, request, view):

#         if request.method in permissions.SAFE_METHODS:
#             return True
#         else:
#             return bool(request.user and request.user.is_staff)
        
    
class IsManager(permissions.BasePermission):
    
    def has_permission(self, request, view):

        if request.method in ['GET', 'POST', 'PUT', 'DELETE']:
            return bool(request.user.role.name == 'Manager')    
        
        
class IsHR(permissions.BasePermission):
    
    def has_permission(self, request, view):

        if request.method in ['GET', 'POST', 'PUT', 'DELETE']:
            return bool(request.user.role.name == 'HR')    
        

class IsEmployeeOrManager(permissions.BasePermission):
    
    def has_permission(self, request, view):

        if request.method in ['GET', 'POST', 'PUT', 'DELETE']:
            return bool(request.user.role.name in ['Employee', 'Manager'])    