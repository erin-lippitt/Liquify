# Landsat 8 data loading functions

import os
from glob import glob
import rioxarray as rxr
import earthpy as et
import matplotlib.pyplot as plt

def load_data(file_path=None,earthpy_subset=None):
    '''
    Load .tif file stack either from an earthpy subset or already downloaded files.
    
    Parameters
    ----------
    (choose one or the other data locations to load from)
    file_path: str
        name of folder containing .tif files
    earthpy_subset: str
        name or url of earthpy data user wants to download
        
    Returns
    -------
    data_stack: 
        stack of .tif  files in order of Landsat band
    '''
    # Setting working directories and data paths
    if earthpy_subset != None:
        data = et.data.get_data(earthpy_subset)
        os.chdir(os.path.join(et.io.HOME,'earth-analytics', 'data'))
        path = os.path.join(earthpy_subset,'landsat_collect','LC080340322016072301T1-SC20180214145802','crop') # generalize
    elif file_path != None:
        os.chdir(os.path.join(et.io.HOME, file_path))
        path = os.path.join(file_path)
    
    # Generating list of .tif files and sorting by band (based on Landsat file naming structure)
    data_stack = glob(os.path.join(path,'*band*.tif'))
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

def implot(image,title=None,figsize=(15,13),cmap='Greys_r'):
    '''
    Plot an image, setting default options and easy tweaking of parameters
    
    Parameters
    ----------
    image: array_like
        2D array containing an image to be plotted
    title: str
        title of plot
    figsize: tuple, optional
        figure size to use. Default: (15,13)
    cmap: str, optional
        Colormap to use for the image. Default: 'Greys_r'
    **kwargs
        Additional arguments are passed to matplotlib plotting commands. Currently supported: vmin, vmax.
        
    Returns
    -------
    fig, ax
        figure and axes objects containing currently plotted data.
    '''
    fig, ax = plt.subplots(figsize=figsize)
    image.plot.imshow(ax=ax,cmap=cmap)
    ax.set_axis_off()
    
    if title != None:
        ax.set_title(title,fontsize=15)
    #ax.tick_params(direction='in',length=9,width=1.5,labelsize=15)
    return fig, ax