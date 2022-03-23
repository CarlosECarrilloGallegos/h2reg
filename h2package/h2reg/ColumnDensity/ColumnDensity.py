import numpy as np
from astropy.io import fits
from astropy import units as u
import math
import matplotlib.pyplot as plt
from spectral_cube import SpectralCube
from astropy.wcs import WCS


def CD_Pineda(iim, Tex, max_map):
    '''
    Function returns column density map of data cube using the method in Kong et. al
    2019 (Pineda eqn 7/9).
    
    NOTE: We assume Tex of 12Co can be used for Tex 13CO as well.
    
    !!: currently set up for 13CO data only
    
    Parameters
    ---------------
    iim: 2d array
        Integrated intensity map of data
    tex: 2d array
        Excitation temperature map of data
    max_map: 2d array
        Map of maximum values of the data
    
    Returns
    --------------
    CD_Kong:
        Column Density map of data 
        
    '''
    
    
    #Evaluate Taue using Pineda equation 7
    Tau = -np.log(1- (max_map / 5.3) / (1/(np.exp(5.3/Tex) -1) -0.16))
    
    #Now Bourke eqn 5
    
    CD = ((Tau/(1 - np.exp(-Tau))) * (3*10**14) * (iim/(1-np.exp(-5.3/Tex))))
    
    return CD


def CD_Pineda_opticthin(iim, Tex, max_map):
    '''
    Function returns column density map of data cube using the method in Kong et. al
    2019 (Pineda eqn 7/9). We assume optically thin and omit the leading coefficient in Pineda
    eqn. 9.
    
    NOTE: We assume Tex of 12Co can be used for Tex 13CO as well.
    
    !! currently set up for 13CO data only
    
    Parameters
    ---------------
    iim: 2d array
        Integrated intensity map of data
    tex: 2d array
        Excitation temperature map of data
    max_map: 2d array
        Map of maximum values of the data
    
    Returns
    --------------
    CD_Kong:
        Column Density map of data 
        
    '''
        
    #Evaluate Taue using Pineda equation 7
    Tau = -np.log(1- (max_map / 5.3) / (1/(np.exp(5.3/Tex) -1) -0.16))
    
    #Now Bourke eqn 5
    
    CD = (3*10**14) * (iim/(1-np.exp(-5.3/Tex)))
    
    return CD