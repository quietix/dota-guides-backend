from rest_framework import permissions

class IsAdminOrSelf(permissions.BasePermission):
    """
    Custom permission to only allow admins or the user themselves to access the user data.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.user == obj
