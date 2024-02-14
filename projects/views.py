from rest_framework import viewsets
from .models import Project, Link
from .serializers import ProjectSerializer, LinkSerializer

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
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

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
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
