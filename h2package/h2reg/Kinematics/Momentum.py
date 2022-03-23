def momentum(velocity, mass):
    '''
    Returns momentum of the region in units of Solar Mass * km/s
    
    Parameters
    -------------
    
    velocity: float
        velocity of peak emission of HII Region in meters
        
    mass: float
        mass of HII Region in kg
        
    Returns
    ---------------
    p: float
        momentum of HII Region in solar mass * km/s
        
    
    '''
    #Convert to km and solar masses
    Solar_Mass = 1.989e30 #kg
    mass = mass / Solar_Mass #solar masses
    velocity = velocity / 1000. #kilometers
    
    p = mass * velocity
    
    return p
