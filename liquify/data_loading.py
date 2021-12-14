# Landsat 8 data loading functions

import os
from glob import glob
import rioxarray as rxr
import earthpy as et

def load_data(file_path=None,earthpy_subset=None):
    '''
    Load .tif file stack either from an earthpy subset or already downloaded files.
    
    Parameters
    ----------
    (choose one or the other data locations to load from)
    file_path: str
        name of folder containing .tif files
    earthpy_subset: str
        name of earthpy data user wants to download
        
    Returns
    -------
    data_stack: 
        stack of .tif  files in order of Landsat band
    '''
    # Setting working directories and data paths
    if earthpy_subset != None:
        data = et.data.get_data(earthpy_subset)
        os.chdir(os.path.join(et.io.HOME,'earth-analytics', 'data'))
        path = os.path.join(earthpy_subset)
    elif file_path != None:
        os.chdir(os.path.join(et.io.HOME, file_path))
        path = os.path.join(file_path)
    
    # Generating list of .tif files and sorting by band (based on Landsat file naming structure)
    data_stack = glob(os.path.join(path,'*.tif'))
    data_stack.sort()
    return data_stack

def load_band(data_stack,ext):
    '''
    Load a specific band of a given dataset. Assumes bands are in order.
    
    Parameters
    ----------
    data_stack:
        stack of .tif files in order of satellite band
    ext: int
        band user wants to select
        
    Return
    ------
    band: array-like
        image data of selected band from dataset
    '''
    band = rxr.open_rasterio(data_stack[ext], masked=True).squeeze() # squeeze makes sure it's returning a 2d arr
    return band