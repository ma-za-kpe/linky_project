from rest_framework import viewsets, permissions
from .models import Project, Link, Team
from .permissions import IsOwnerOrReadOnly, IsMemberOfTeam
from .serializers import ProjectSerializer, LinkSerializer, TeamSerializer
from rest_framework.pagination import PageNumberPagination

class ProjectsViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides CRUD operations for projects.

    retrieve:
    Return a specific project instance.

    list:
    Return a list of all projects.

    create:
    Create a new project instance.

    update:
    Update an existing project instance.

    partial_update:
    Partially update an existing project instance.

    destroy:
    Delete a project instance.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = PageNumberPagination


class LinkViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides CRUD operations for links.

    retrieve:
    Return a specific link instance.

    list:
    Return a list of all links.

    create:
    Create a new link instance.

    update:
    Update an existing link instance.

    partial_update:
    Partially update an existing link instance.

    destroy:
    Delete a link instance.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    pagination_class = PageNumberPagination


class TeamViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides CRUD operations for Teams.

    retrieve:
    Return a specific Team instance.

    list:
    Return a list of all Teams.

    create:
    Create a new Team instance.

    update:
    Update an existing Team instance.

    partial_update:
    Partially update an existing Team instance.

    destroy:
    Delete a Team instance.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    pagination_class = PageNumberPagination
    