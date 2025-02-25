import geopandas as gpd
from shapely.geometry import MultiPolygon, Polygon, LineString

# Load the parcels and water data
parcels = gpd.read_file('parcels_small.geojson')
water = gpd.read_file('water.geojson')

# Print the number of items in each data array
print(f"Number of parcels: {len(parcels)}")
print(f"Number of water features: {len(water)}")

# Ensure all geometries are MultiPolygon
def to_multipolygon(geom):
    if isinstance(geom, Polygon):
        return MultiPolygon([geom])
    elif isinstance(geom, MultiPolygon):
        return geom
    elif isinstance(geom, LineString):
        return MultiPolygon([geom.buffer(0.001)])  # Buffer to convert LineString to Polygon
    else:
        return None  # Filter out non-polygon geometries

parcels['geometry'] = parcels['geometry'].apply(to_multipolygon)
water['geometry'] = water['geometry'].apply(to_multipolygon)

# Drop rows with None geometries
parcels = parcels[parcels['geometry'].notnull()]
water = water[water['geometry'].notnull()]

# Find intersections
intersections = gpd.overlay(parcels, water, how='intersection')

# Print or save the results
print(intersections)
