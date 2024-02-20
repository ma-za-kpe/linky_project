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
    print(f"chart_params: {chart_params}")
    # print(ee.data.getThumbURL({
    #     'width': 800,
    #     'height': 400,
    #     'bands': 'NDVI',
    #     'region': roi,
    #     'chartParams': chart_params
    # }))

# def ndvi_gen(polygon: List[Coord], width: int, date_start: int, date_end: int) -> Dict[str, Union[int, float, str, List[Coord], str]]:
#     service_account = 'agriguard-hack@agriguard-414623.iam.gserviceaccount.com'
#     # TODO: Add your service account credentials here, keep the in .evn file
#     credentials = ee.ServiceAccountCredentials(service_account, 'ndvi/.private-key.json')
#     ee.Initialize(credentials)
#     # Load a Landsat image.
#     # img = ee.Image('LANDSAT/LT05/C02/T1_L2/LT05_034033_20000913')
#     # Print image object WITHOUT call to getInfo(); prints serialized request instructions.
#     # print(f"img without getInfo: {img}")
    
    # # Extract latitude and longitude values from the polygon
    # # Convert polygon coordinates to Earth Engine format
    # coord = [[a['lng'], a['lat']] for a in polygon]
    # coord_lng = [a['lng'] for a in polygon]
    # coord_lat = [a['lat'] for a in polygon]
    
    # # Calculate the maximum and minimum longitude and latitude
    # # Calculate bounding box coordinates
    # max_lng = max(coord_lng)
    # min_lng = min(coord_lng)
    # max_lat = max(coord_lat)
    # min_lat = min(coord_lat)
    
    # # Calculate the delta longitude and latitude
    # # Calculate image dimensions based on width and aspect ratio of the polygon
    # # delta_lng is the difference between the maximum longitude (max_lng) and the minimum longitude (min_lng).
    # # delta_lat is the difference between the maximum latitude (max_lat) and the minimum latitude (min_lat).
    # delta_lng = max_lng - min_lng
    # delta_lat = max_lat - min_lat
    
    # # Calculate the dimensions of the image
    # dimension_lng = round(width)
    # dimension_lat = round((width * delta_lat) / delta_lng)
    
    # # Calculate the centroid longitude and latitude
    # # Calculate centroid of the polygon
    # centroid_lng = get_polygon_centroid(polygon)['lng']
    # centroid_lat = get_polygon_centroid(polygon)['lat']
    
    
    # # Create Earth Engine point geometry for centroid
    # point = ee.Geometry.Point([centroid_lng, centroid_lat])

    # # Load Landsat 8 NDVI image collection
    # l8 = ee.ImageCollection('LANDSAT/LC08/C01/T1_32DAY_NDVI')


#     # Define color palette for NDVI visualization
    # palette = {
    #     'ndviAgro': [
    #         'd7d7d7', 'd5d5d5', 'd2d2d2', 'c7c7c7', 'a70204', 'e50004',
    #         'fb6300', 'ffb001', 'f5e702', 'c2e100', '81cd00', '5cbe02',
    #         '46a703', '36a801', '209e01', '029302', '008900', '027e02',
    #         '047101', '006400'
    #     ]
    # }
    
    
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


# def ndvi_gen(dev_key: Dict[str, str], polygon: List[Coord], width: int, date_start: int, date_end: int) -> Dict[str, Union[int, float, str, List[Coord], str]]:
#     ee.Initialize()

#     coord = [[a['lng'], a['lat']] for a in polygon]
#     coord_lng = [a['lng'] for a in polygon]
#     coord_lat = [a['lat'] for a in polygon]

#     max_lng = max(coord_lng)
#     min_lng = min(coord_lng)
#     max_lat = max(coord_lat)
#     min_lat = min(coord_lat)

#     delta_lng = max_lng - min_lng
#     delta_lat = max_lat - min_lat

#     dimension_lng = round(width)
#     dimension_lat = round((width * delta_lat) / delta_lng)

#     centroid_lng = get_polygon_centroid(polygon)['lng']
#     centroid_lat = get_polygon_centroid(polygon)['lat']

#     point = ee.Geometry.Point([centroid_lng, centroid_lat])

#     l8 = ee.ImageCollection('LANDSAT/LC08/C01/T1_32DAY_NDVI')

#     palette = {
#         'ndviAgro': [
#             'd7d7d7', 'd5d5d5', 'd2d2d2', 'c7c7c7', 'a70204', 'e50004',
#             'fb6300', 'ffb001', 'f5e702', 'c2e100', '81cd00', '5cbe02',
#             '46a703', '36a801', '209e01', '029302', '008900', '027e02',
#             '047101', '006400'
#         ]
#     }

#     image = ee.Image(
#         l8
#         .filterDate(date_start, date_end)
#         .sort('CLOUD_COVER')
#         .first()
#     )

#     time_start = image.get('system:time_start').getInfo()
#     time_end = image.get('system:time_end').getInfo()
#     index = image.get('system:index').getInfo()

#     if index:
#         vis = image.visualize({
#             'bands': ['NDVI'],
#             'min': -0.2,
#             'max': 0.8,
#             'opacity': 1,
#             'palette': palette['ndviAgro']
#         }).clip(ee.Geometry.Polygon(coord))

#         url_img = vis.getThumbURL({
#             'dimensions': [dimension_lng, dimension_lat],
#             'region': ee.Geometry.Polygon(coord)
#         })

#     ret = {
#         'width': dimension_lng,
#         'height': dimension_lat,
#         'centroid': {'lng': centroid_lng, 'lat': centroid_lat},
#         'bounds': [
#             {'lng': max_lng, 'lat': max_lat},
#             {'lng': min_lng, 'lat': min_lat}
#         ],
#         'time_start': time_start,
#         'time_end': time_end,
#         'index': index,
#         'img_url': url_img if index else None
#     }

#     return ret

# def get_polygon_centroid(pts: List[Coord]) -> Coord:
#     first = pts[0]
#     last = pts[-1]
#     if first['lng'] != last['lng'] or first['lat'] != last['lat']:
#         pts.append(first)
#     area = 0
#     lng = 0
#     lat = 0
#     n_pts = len(pts)
#     for i in range(n_pts):
#         p1 = pts[i]
#         p2 = pts[i - 1]
#         f = (p1['lat'] - first['lat']) * (p2['lng'] - first['lng']) - (p2['lat'] - first['lat']) * (p1['lng'] - first['lng'])
#         area += f
#         lng += (p1['lng'] + p2['lng'] - 2 * first['lng']) * f
#         lat += (p1['lat'] + p2['lat'] - 2 * first['lat']) * f
#     f = area * 3
#     return {'lng': lng / f + first['lng'], 'lat': lat / f + first['lat']}
