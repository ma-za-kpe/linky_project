from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Ndvi
from .serializers import NdviSerializer
from typing import Dict, Any

from .ndvi_calculation import ndvi_gen

class NdviViewSet(viewsets.ModelViewSet):
    queryset = Ndvi.objects.all()
    serializer_class = NdviSerializer
    
    def create(self, request, *args, **kwargs):
        # Perform the calculation here
        title = request.data.get('title')
        polygon = request.data.get('polygon')
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')
        
        # Calculate NDVI
        ndvi_value = self.calculate_ndvi(title, polygon, start_date, end_date)
        
        # Perform your calculation logic here, for example:
        # ndvi_value = 42.0  # Replace this with your actual calculation
        
        # Create a new Ndvi instance with the calculated value
        ndvi = Ndvi.objects.create(
            title=title,
            polygon=polygon,
            start_date=start_date,
            end_date = end_date,
            ndvi=ndvi_value  # Assuming 'ndvi' is the field to store the calculation result
        )
        
        # Serialize the new instance
        serializer = self.get_serializer(ndvi)
        
        # Return a successful response with the serialized data
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def calculate_ndvi(title: str, polygon: Dict[str, Any], start_date: str, end_date: str) -> float:

        # Call the ndvi_gen function to calculate NDVI
        result = ndvi_gen(polygon['coordinates'][0], 400, int(start_date), int(end_date))  # Assuming width is 400

        # Extract the NDVI value from the result
        # Adjust this according to the actual structure of the result
        ndvi_value = 0.0  # Placeholder value, replace with the actual NDVI value

        return ndvi_value
    