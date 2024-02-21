import ee
from typing import Dict, List, Union

Coord = Dict[str, float]


def chart(polygon: List[Coord], width: int, date_start: str, date_end: str) -> None:
    # Initialize Earth Engine
    service_account = 'agriguard-hack@agriguard-414623.iam.gserviceaccount.com'
    # TODO: Add your service account credentials here, keep the in .evn file
    credentials = ee.ServiceAccountCredentials(service_account, 'ndvi/.private-key.json')
    ee.Initialize(credentials)
    # Load a Landsat image.
    # img = ee.Image('LANDSAT/LT05/C02/T1_L2/LT05_034033_20000913')
    # Print image object WITHOUT call to getInfo(); prints serialized request instructions.
    # print(f"img without getInfo: {img}")
    
    # Extract latitude and longitude values from the polygon
    # Convert polygon coordinates to Earth Engine format
    coord = [[a['lng'], a['lat']] for a in polygon]
    coord_lng = [a['lng'] for a in polygon]
    coord_lat = [a['lat'] for a in polygon]
    
    # Calculate the maximum and minimum longitude and latitude
    # Calculate bounding box coordinates
    max_lng = max(coord_lng)
    min_lng = min(coord_lng)
    max_lat = max(coord_lat)
    min_lat = min(coord_lat)
    
    # Calculate the delta longitude and latitude
    # Calculate image dimensions based on width and aspect ratio of the polygon
    # delta_lng is the difference between the maximum longitude (max_lng) and the minimum longitude (min_lng).
    # delta_lat is the difference between the maximum latitude (max_lat) and the minimum latitude (min_lat).
    delta_lng = max_lng - min_lng
    delta_lat = max_lat - min_lat
    
    # Calculate the dimensions of the image
    dimension_lng = round(width)
    dimension_lat = round((width * delta_lat) / delta_lng)
    
    # Calculate the centroid longitude and latitude
    # Calculate centroid of the polygon
    centroid_lng = get_polygon_centroid(polygon)['lng']
    centroid_lat = get_polygon_centroid(polygon)['lat']
    
    
    # Create Earth Engine point geometry for centroid
    roi = ee.Geometry.Point([centroid_lng, centroid_lat])

    # Load Landsat 8 NDVI image collection
    l8 = ee.ImageCollection('LANDSAT/LC08/C01/T1_32DAY_NDVI')

    # # Filter the collection by date range
    # collection = l8.filterDate(date_start, date_end)

    # Map function to calculate cloud-masked NDVI
    def calculate_ndvi(image):
        cloud = ee.Algorithms.Landsat.simpleCloudScore(image).select('cloud')
        mask = cloud.lte(20)
        ndvi = image.normalizedDifference(['B5', 'B4']).rename('NDVI')
        return image.addBands(ndvi).updateMask(mask)

    cloudlessNDVI = l8.map(calculate_ndvi)

    # Define the chart parameters
    chart_params = {
        'imageCollection': cloudlessNDVI.select('NDVI'),
        'region': roi,
        'reducer': ee.Reducer.first(),
        'scale': 30
    }

    # Print the chart
    # print(f"chart_params: {chart_params}")
    
    # Function to reduce an image to a mean value in the region of interest
    def reduce_image(image):
        value = image.reduceRegion(reducer=ee.Reducer.mean(), geometry=roi, scale=30)
        return ee.Feature(None, {'date': image.date().format('YYYY-MM-dd'), 'ndvi': value.get('NDVI')})

    # Reduce the ImageCollection to a time series for the region of interest
    timeseries = l8.map(reduce_image)

    # Get the NDVI values as a list
    ndviData = timeseries.getInfo()['features']

    # Print the extracted NDVI data
    # print(f"chart ndviData: {ndviData}")
    
    return ndviData
    
# Function to calculate centroid of a polygon
def get_polygon_centroid(pts: List[Coord]) -> Coord:
    first = pts[0]
    last = pts[-1]
    if first['lng'] != last['lng'] or first['lat'] != last['lat']:
        pts.append(first)
    area = 0
    lng = 0
    lat = 0
    n_pts = len(pts)
    for i in range(n_pts):
        p1 = pts[i]
        p2 = pts[i - 1]
        f = (p1['lat'] - first['lat']) * (p2['lng'] - first['lng']) - (p2['lat'] - first['lat']) * (p1['lng'] - first['lng'])
        area += f
        lng += (p1['lng'] + p2['lng'] - 2 * first['lng']) * f
        lat += (p1['lat'] + p2['lat'] - 2 * first['lat']) * f
    f = area * 3
    return {'lng': lng / f + first['lng'], 'lat': lat / f + first['lat']}
