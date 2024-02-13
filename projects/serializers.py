from rest_framework import serializers
from .models import Project, Link        
        
class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id','url', 'title', 'description', 'date_added', 'tags']

class ProjectSerializer(serializers.ModelSerializer):
    links = LinkSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'created_by', 'date_created', 'last_modified', 'visibility', 'links']