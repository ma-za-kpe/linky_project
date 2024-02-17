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
        return obj.added_by == request.user

class IsMemberOfTeam(permissions.BasePermission):
    """
    Custom permission to only allow members of a team to view or modify it.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the user is a member of the team
        return request.user in obj.members.all()




# sAuthenticated: This permission class ensures that the user is authenticated before granting access to the viewset. This is useful for ensuring that only logged-in users can perform actions like creating projects, adding links, or managing teams.

# IsOwnerOrReadOnly: Custom permission class that allows only the owner of an object (e.g., project, link) to modify it. Other users can view the object but cannot make changes to it.

# IsMemberOfTeam: Custom permission class that allows only members of a team to view or modify the team. This is useful for ensuring that only team members can manage the team's details.

# IsAdminUser: This permission class restricts access to admin users only. Admin users have full control over the app and can perform actions that regular users cannot.
