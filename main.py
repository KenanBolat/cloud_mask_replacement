import numpy as np
import datetime
import pandas as pd
from osgeo import gdal
import os
import matplotlib.pyplot as plt


def read_raster_data(filename):
    if os.path.isfile(filename):
        return gdal.Open(filename)
    else:
        assert f'File {filename} does not exists'


if __name__ == '__main__':
    processing_path = r'./data'
    scl_filename = 'imageExample_SCL.tif'
    bads_filename = 'imageExample_Bands.tif'
    file_scl = os.path.join(processing_path, scl_filename)
    file_bands = os.path.join(processing_path, bads_filename)

    print(file_scl, file_bands)

    raster1 = read_raster_data(file_scl)
    raster2 = read_raster_data(file_bands)
    # a = raster1.GetRasterBand(1).ReadAsArray()
    pass
