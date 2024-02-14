from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.created_by == request.user

class IsMemberOfTeam(permissions.BasePermission):
    """
    Custom permission to only allow members of a team to view or modify it.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the user is a member of the team
        return request.user in obj.members.all()
