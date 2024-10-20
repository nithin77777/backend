from rest_framework import permissions

class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Authenticated users only can see list view
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        
        if request.method == 'POST':
            return request.user and request.user.is_authenticated
        
        return request.user and request.user.is_authenticated

    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request so we'll always
        # allow GET, HEAD, or OPTIONS requests  
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user == obj.owner
       