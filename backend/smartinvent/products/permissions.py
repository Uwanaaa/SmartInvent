from rest_framework.permissions import BasePermission

class isAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role=='Admin'
    

class isActive(BasePermission):
    def is_active(self,request,view):
        return request.user.is_authenticated and request.user.is_active == True