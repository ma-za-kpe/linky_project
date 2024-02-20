from rest_framework import serializers
from .models import Tags

# TODO: perfomance issue, use serializers.Serializer.
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name')
        model = Tags