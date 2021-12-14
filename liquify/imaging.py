# Optional imaging functions to accompany liquify

import matplotlib.pyplot as plt
import earthpy.plot as ep

def implot(image,title=None,figsize=(15,13),cmap='Greys_r'):
    '''
    Plot an image, setting default options and easy tweaking of parameters
    
    Parameters
    ----------
    image: array_like
        2D array containing an image to be plotted
    title: str, optional
        title of plot
    figsize: tuple, optional
        figure size to use. Default: (15,13)
    cmap: str, optional
        Colormap to use for the image. Default: 'Greys_r'
        
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
    return fig, ax

def water_plot(image,tick_loc,title=None,figsize=(15,13),cmap=plt.cm.get_cmap('Blues', 2)):
    '''
    Plot with labeled water and non-water regions, setting default options and easy tweaking of parameters
    
    Parameters
    ----------
    image: array_like
        2D array containing an image to be plotted
    tick_loc: tuple
        where on colorbar to label (water, not water) based on data values of image
    title: str
        title of plot
    figsize: tuple, optional
        figure size to use. Default: (15,13)
    cmap: str, optional
        Colormap to use for the image. Default: 'Greys_r'
        
    Returns
    -------
    fig, ax
        figure and axes objects containing currently plotted data.
    '''
    fig, ax = plt.subplots(figsize=figsize)

    im = ax.imshow(image,cmap=cmap)

    cbar = ep.colorbar(im)
    cbar.set_ticks(tick_loc)
    cbar.ax.set_yticklabels(['Land', 'Water'])

    if title != None:
        ax.set_title(title,fontsize=15)
    
    ax.set_axis_off()
    return fig, ax