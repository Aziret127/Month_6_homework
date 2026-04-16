from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwner(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        if request.method == "POST" and request.user.is_staff:
            return False
        return True
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        
        owner = getattr(obj, 'owner', None)
        return owner == request.user
    

class IsAnonymous(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS 