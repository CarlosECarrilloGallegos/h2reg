import numpy as np
from astropy.io import fits
from astropy import units as u
import math
import matplotlib.pyplot as plt
from spectral_cube import SpectralCube
from astropy.wcs import WCS
from pvextractor import extract_pv_slice
from pvextractor import Path
from astropy.coordinates import SkyCoord
from astropy.coordinates import FK5
from reproject import reproject_interp

def PV_Extract(RA_min, RA_max, Dec_min, Dec_max, width, fits_cube):
    '''
    Creates position-velocity slice given Right Ascencion and Declination limits, the width of the slice
    in arcseconds, and the fits cube
    
    PARAMETERS
    --------------------
    RA_min/RA_max: string
        Lowest and highest right ascension used to bound the region.
        Use format: "00h00m00s'
    Dec_min/Dec_max: string
        Lowest and highest declinations used to bound the region.
        Use format: "0d00m00.0s"
    width: int
        Desired width of slice in arcseconds
    fits_cube: 3D Data cube
        Fits cube to slice (must have WCS)
        
    RETURNS
    ---------------------
    PV_slice: 2d-fits image
        Position-Velocity Diagram of region
    
    '''
    
    coordmin = SkyCoord(RA_min, Dec_min)
    coordmax = SkyCoord(RA_max, Dec_max)
    
    coords = FK5([coordmin.ra.deg, coordmax.ra.deg] * u.deg, [coordmin.dec.deg, coordmax.dec.deg] * u.deg)
    
    path = Path(coords, width = width * u.arcsec)
    
    PV_slice = extract_pv_slice(fits_cube, path)
    
    return PV_slice