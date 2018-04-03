from sentinelsat.sentinel import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date

api = SentinelAPI('user', 'password', 'https://scihub.copernicus.eu/dhus')

# download single scene by known product id
#api.download(<product_id>)

# search by polygon, time, and SciHub query keywords
footprint = geojson_to_wkt(read_geojson('geojson/eastgreenland.geojson'))
products = api.query(footprint,
                     date=('20151219', date(2015, 12, 29)),
                     platformname='Sentinel-1',
                     cloudcoverpercentage=(0, 30))

# download all results from the search
#api.download_all(products)
#
## GeoJSON FeatureCollection containing footprints and metadata of the scenes
#api.to_geojson(products)
#
## GeoPandas GeoDataFrame with the metadata of the scenes and the footprints as geometries
#api.to_geopandas(products)

# Get basic information about the product: its title, file size, MD5 sum, date, footprint and
# its download url
#api.get_product_odata(<product_id>)

# Get the product's full metadata available on the server
#api.get_product_odata(<product_id>, full=True)