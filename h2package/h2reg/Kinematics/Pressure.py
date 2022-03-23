import math

def turbulence_pressure(sigma_turb, radius, mass):
    '''
    Calculates the turbulence pressure of M43 given the sigma at peak emission, mass, and the 
    radius of the shell, assuming spherical conditions
    
    Parameters
    ---------------
    sigma_turb: float
        sigma at peak emission
    radius: float
        radius of the region in meters
    mass: float
        mass of the region in kg
        
    Returns
    ---------------
    
    turbulence_pressure: float
        Turbulence pressure of the region
    '''
    
    volume = 4/3 * math.pi * radius**3
    
    density = mass / volume
    
    turbulence_pressure = density * sigma_turb**2
    
    return turbulence_pressure


def radiation_pressure(star_luminosity, radius):
    '''
    Calculates the radiation pressure of a region given the luminosity of its ionizing star and its radius
    
    Parameters
    --------------
    star_luminosity: float
        luminosity of the star in joules/second
    radius: float
        radius of the region in meters
    
    Returns
    --------------
    radiation_pressure:
        radiation pressure of the region
    
    '''
    
    #define constants
    c = 3e8 #m/s
    
    radiation_pressure = star_luminosity/(4*math.pi * radius**2 * c)
    
    return radiation_pressure

def thermal_pressure
    