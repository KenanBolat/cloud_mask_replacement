import numpy as np
import datetime
import pandas as pd
import xarray as xr
# import rasterio
from osgeo import gdal
import os
import matplotlib.pyplot as plt
import enum
import rioxarray
import datetime

"""
Classification according to the classification mask generation defined in the following documentation
https://sentinels.copernicus.eu/web/sentinel/technical-guides/sentinel-2-msi/level-2a/algorithm

"""
NO_DATA = 0
SATURATED_OR_DEFECTIVE = 1
CAST_SHADOWS = 2
CLOUD_SHADOWS = 3
VEGETATION = 4
NOT_VEGETATED = 5
WATER = 6
UNCLASSIFIED = 7
CLOUD_MEDIUM_PROBABILITY = 8
CLOUD_HIGH_PROBABILITY = 9
THIN_CIRRUS = 10
SNOW_or_ICE = 11

"""Define functions to read the given data."""


def read_raster_data_gdal(filename):
    """Function the read the raster using gdal"""
    if os.path.isfile(filename):
        raster = gdal.Open(filename)
        return raster.GetRasterBand(1).ReadAsArray()
    else:
        assert f'File {filename} does not exists'


def read_raster_data_xr(filename):
    """Function the read the raster using xarray"""
    if os.path.isfile(filename):
        return rioxarray.open_rasterio(filename)
    else:
        assert f'File {filename} does not exists'


def apply_cloud_mask(image_filename, scl_mask_filename):
    # Read Dataset using rasterio
    scl_dataset = read_raster_data_xr(scl_mask_filename)
    bands_dataset = read_raster_data_xr(image_filename)

    # define filter for the given
    filter = (scl_dataset == VEGETATION) | (scl_dataset == NOT_VEGETATED) | (scl_dataset == UNCLASSIFIED)

    # Create mask using xarray filtering "where" method with required classifications
    mask = scl_dataset.where(filter, 0)

    # Export mask for visual comparison with the external GIS Applications
    mask.rio.to_raster(os.path.join(processing_path, 'mask.tif'))

    # Apply mask to the bands
    masked_bands = bands_dataset.where(filter.values, 0)

    # Export masked out bands to a multilayered geotiff
    masked_bands.rio.to_raster(os.path.join(processing_path, 'masked_bands.tif'))


if __name__ == '__main__':
    start = datetime.datetime.now()
    processing_path = r'./data'
    scl_filename = 'imageExample_SCL.tif'
    bads_filename = 'imageExample_Bands.tif'
    file_scl = os.path.join(processing_path, scl_filename)
    file_bands = os.path.join(processing_path, bads_filename)

    print(file_scl, file_bands)

    raster1 = read_raster_data_gdal(file_scl)
    raster2 = read_raster_data_gdal(file_bands)

    apply_cloud_mask(file_bands, file_scl)
    print('Execution time for the first method:', str(datetime.datetime.now() - start))


    pass
