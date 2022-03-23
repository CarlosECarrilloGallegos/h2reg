from astropy.io import fits
def load_fits(filename, *args):
    '''
    A function that takes in a FITS file and returns a python-useable array .
    
    Parameters
    ------------------
    
    filename: string
        name of the fits file
    *args: int
        Extension of file, if desired
    
    Returns
    ------------------
    (header, data)
        Tuple containing the header and data of the fits file

    '''
    
    
    fits_file = fits.open(filename)
    #header = fits_file[0].header
    #data = fits_file[0].data
    
    
    #return(header, data)
    return fits_file
