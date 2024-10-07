from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object or superusers to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Write permission is only allowed to the owner of the object or superusers
        return obj.created_by == request.user or request.user.is_superuser

    def has_permission(self, request, view):
        # Allow any user to view the list but restrict modifications
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated
