from rest_framework import serializers
from .models import Ndvi
        
class NdviSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ndvi
        fields = '__all__'