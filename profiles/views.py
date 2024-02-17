from rest_framework import viewsets, permissions
from .models import Profile
from .serializers import ProfileSerializer
from projects.permissions import IsOwnerOrReadOnly

class ProfileViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides CRUD operations for profiles.

    retrieve:
    Return a specific profile instance.

    list:
    Return a list of all profiles.

    create:
    Create a new profile instance.

    update:
    Update an existing profile instance.

    partial_update:
    Partially update an existing profile instance.

    destroy:
    Delete a profile instance.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
