from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'

class IsOfficeStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'office_staff'

class IsLibrarian(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'librarian'
