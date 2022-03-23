def KE(velocity, mass):
    '''
    Returns kinetic energy of system given mass and velocity of peak emission
    
    Parameters
    --------------
    velocity: float
        Velocity of peak emission of the HII Region in m/s
        
    mass: float
        mass of the region in KG
    
    Returns
    --------------
    
    KineticEnergy: float
        KE of the region in ergs
    '''
    KineticEnergy = 0.5 * mass * velocity**2
    return KineticEnergy