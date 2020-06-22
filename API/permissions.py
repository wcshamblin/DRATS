from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class IsAuthenticated(permissions.BasePermission):
    # Allows access only to authenticated users.
    def has_permission(self, request, view):
        message = 'You must be authenticated'
        is_it = bool(request.user and request.user.is_authenticated)
        if is_it:
            return is_it
        else:
            raise PermissionDenied(detail=message)