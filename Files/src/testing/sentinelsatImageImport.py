# connect to the API
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date

api = SentinelAPI('kongstad', 'Delphini1', 'https://scihub.copernicus.eu/dhus')

# search by polygon, time, and SciHub query keywords
footprint = geojson_to_wkt(read_geojson('geojson/scoresbysund_small.geojson'))
products = api.query(footprint,
                     date=('20170826', date(2017, 8, 30)),
                     platformname='Sentinel-2',
                     cloudcoverpercentage=(0,5))


api.to_geojson(products)
# download all results from the search
api.download_all(products,'sentinel2images/')