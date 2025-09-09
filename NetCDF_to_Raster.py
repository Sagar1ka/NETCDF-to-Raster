
from pathlib import Path
import xarray as xr
import rioxarray as rio
import geopandas as gpd
from shapely.geometry import mapping

# User-defined paths
shapefile = "C:/Users/GIS/TerraAET/Rheinland.shp"
netcdf_path = Path("C:/Users/GIS/TerraAET/Input/")
output_path = Path("C:/Users/GIS/TerraAET/Output_raster/")

# Create output folder if not exists
output_path.mkdir(parents=True, exist_ok=True)

# Get list of NetCDF files
files = list(netcdf_path.glob("*.nc"))

# Months
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Load shapefile
shp = gpd.read_file(shapefile)

for nc_file in files:
    # Open NetCDF
    ds = xr.open_dataset(nc_file)

    # Extract variable
    ET = ds['aet']

    # Provide spatial axis
    ET = ET.rio.set_spatial_dims('lon', 'lat')

    # Set CRS
    ET = ET.rio.set_crs("epsg:4326")

    # Clip data with shapefile
    ET_clipped = ET.rio.clip(shp.geometry.apply(mapping), shp.crs)

    # Loop through time dimension (assuming 12 months)
    for k in range(len(ET_clipped.time)):
        out_file = output_path / f"{nc_file.stem}_{months[k]}.tiff"

        ET_clipped.isel(time=k).rio.to_raster(out_file)
