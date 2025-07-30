from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'
    
# class IsStaffWithLimitedAccess(BasePermission):
#     def has_permission(self, request, view):
#         if request.method in SAFE_METHODS:
#             return True
#         if request.method in ['POST', 'PUT', 'PATCH']:
#             return request.user.is_authenticated and request.user.role == 'staff'
#         return False


class IsAdminOrStaff(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.role == 'admin' or request.user.role == 'staff'