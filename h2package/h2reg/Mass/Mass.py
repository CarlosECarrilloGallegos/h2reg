import numpy as np
from astropy.io import fits
from astropy import units as u
import math
import matplotlib.pyplot as plt
from spectral_cube import SpectralCube
from astropy.wcs import WCS

def pixelarea(distance, pixel_width_arcsec):
    '''
    Area of a pixel in the region in cm^2
    
    Parameters
    ----------------
    distance: float
        distance of the region from Earth in parsecs
        
    pixel_width_arcsec: float
        width of the pixel in arcseconds
        
    Returns
    -----------------
    
    pixel_area: float
        pixel area in cm^2 (because column density will be calculated per cm^2)
    '''
    
    #Convert units to cm and degrees
    distance = distance * 3.08e18.
    pixel_width_degrees = pixel_width_arcsec / 3600.
    
    width = math.tan(pixel_width_degrees) * distance
    
    pixel_area = width**2
    
    return pixel_area
    


def MassEstimate13CO(CD, Region, pixel_area):
    '''
    13CO mass estimate using Bourke et. al eqn. A11
    
    Parameters
    -------------
    CD: 2d array
        Column Density Map
    Region: pyregion object
        Ds9 Region
    pixel_area: float
        Area of pixel in cm^2
        
    Returns
    --------------
    Mass: float
        kg mass of region
    '''
    
    #Variables
    
    H_13CO_Conversion = 7e5
    Area = pixel_area #cm^2 #Area of a pixel in the image
    #Make distance variable ^^
    u_m = 4.5*10**(-27) #kg

    #Load in and Mask the CD of 12CO
    region1 = Region

    fdata = CD[0].data
    f = CD

    #1
    region2 = region1.as_imagecoord(f[0].header)

    mymask = region2.get_mask(hdu=f[0])

    real_mask = mymask * fdata

    #fits.writeto("13CO_CD_Masked.fits", real_mask)

    CO_13_masked = real_mask

    #Compute the mass per pixel via eqn. A11
    Mass_per_pixel = H_13CO_Conversion * Area* u_m *CO_13_masked 

    #Sum all the values in the 2D array, that will give the mass
    Mass = np.sum(Mass_per_pixel)

    return Mass
