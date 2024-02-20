import ee
from typing import Dict, List, Union

Coord = Dict[str, float]

def ndvi_gen(polygon: List[Coord], width: int, date_start: int, date_end: int) -> Dict[str, Union[int, float, str, List[Coord], str]]:
    ee.Authenticate()
    ee.Initialize(project='my-project')
    print(ee.Image("NASA/NASADEM_HGT/001").get("title").getInfo())

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
