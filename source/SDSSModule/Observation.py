import Spectrum
from astropy.io import fits
import numpy as np

class Spectrum (Observation):

    def __init__(self):
        self.flux = None
        self.wavelength = None
        self.plate = None
        self.mjd = None
        self.fibre = None

class Observation:

    def __init__(self, filename):

        self.ra = None      #will be a float
        self.dec = None     #will be a float
        self.redshift = None   #will be a float
        self.timestamp = None   #will be a timestamp
        #self.spectrum = None    #will be a Spectrum object
        self.plate = None
        self.mjd = None
        self.fibre = None
        self.flux = None    #numpy arrays of length X
        self.wavelength = None   #numpy arrays of length X (same as above)

        #Load fits file, called filename
        #load into the above variables

        hdulist = fits.open(filename)
        spectrum = hdulist[1].data
        self.wavelength = np.asarray([10** i[1] for i in spectrum])
        self.flux = np.asarray([i[0] for i in spectrum])
        

    def testing(self):
        print self.wavelength


observation = Observation("filename.txt")
observation.testing()
