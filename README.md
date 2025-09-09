**NetCDF to GeoTIFF Clipping Tool**

This repository provides a Python workflow for clipping NetCDF rasters (e.g., actual evapotranspiration datasets) with a shapefile and exporting them as monthly GeoTIFF files. 

It is designed to help researchers and GIS analysts extract region-specific raster data from global climate and hydrological datasets.

**Features**

-Reads NetCDF files containing geospatial data

-Clips rasters using a shapefile boundary

-Extracts monthly time steps (e.g., 12 months of AET data)

-Saves results as individual GeoTIFFs for each month

-Automatically creates output folders if they do not exist

**Requirements**

The script requires Python 3.x and the following libraries:

pip install xarray rioxarray geopandas shapely

**Usage**

1. Clone this repository:

git clone https://github.com/yourusername/your-repo-name.git


2. Update the paths in the script:** <br>

shapefile = "C:/Users/GIS/TerraAET/Rheinland.shp" <br>
netcdf_path = Path("C:/Users/GIS/TerraAET/Input/")<br>
output_path = Path("C:/Users/GIS/TerraAET/Output_raster/")<br>


3. Run the script:**

python clip_netcdf_to_geotiff.py


4. The clipped GeoTIFFs will be saved in the Output_raster/ folder with filenames like:** <br>

datasetname_Jan.tiff <br>
datasetname_Feb.tiff <br>
...

**File Structure** <br>
📂 your-repo-name<br>
 ┣ 📂 Input          # Folder with NetCDF files (*.nc)<br>
 ┣ 📂 Output_raster  # Output GeoTIFFs will be stored here<br>
 ┣ 📄 Rheinland.shp  # Example shapefile<br>
 ┣ 📄 clip_netcdf_to_geotiff.py  # Main script<br>
 ┗ 📄 README.md<br>

**Example Applications**

-Hydrological modeling (AET, PET, runoff datasets)

-Climate impact studies

-Agricultural water management

-Regional environmental monitoring
