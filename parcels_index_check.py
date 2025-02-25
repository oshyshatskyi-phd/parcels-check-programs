import pandas as pd
import geopandas as gpd
from shapely import wkt

# Load parcels.csv using pandas
data_df = pd.read_csv('parcels.csv')

# Convert the st_astext field to geometry
if 'st_astext' in data_df.columns:
    data_df['geometry'] = data_df['st_astext'].apply(wkt.loads)
    data_gdf = gpd.GeoDataFrame(data_df, geometry='geometry')
else:
    data_gdf = data_df

# Load index_db using geopandas
index_gdf = gpd.read_file('index_db.gpkg')

# Expand the geometries in index_db by 5 meters
index_gdf['geometry'] = index_gdf['geometry'].buffer(5)

# Perform spatial join to find intersecting parcels
intersecting_parcels = gpd.sjoin(data_gdf, index_gdf, how='inner', predicate='intersects')

# Initialize sets to track matching and non-matching cadnums
matching = set()
nonmatching = set()

# Check if cadnum corresponds to zona and kvart fields
for index, row in intersecting_parcels.iterrows():
    # Split cadnum to extract zona and kvart
    cadnum_parts = row['cadnum'].split(':')
    
    if len(cadnum_parts) >= 3:
        zona = cadnum_parts[1]
        kvart = cadnum_parts[2]
        
        # Compare extracted zona and kvart with the corresponding fields
        if int(zona) != int(row['zona']) or int(kvart) != int(row['kvart']):
            nonmatching.add(row['cadnum'])
        else:
            matching.add(row['cadnum'])

# Find cadnums that do not match zona and kvart at all
unmatched = nonmatching - matching
for number in unmatched:
    print(f'Warning: cadnum {number} does not match zona and kvart')

# Print the intersecting parcels to verify
print(intersecting_parcels.head())
