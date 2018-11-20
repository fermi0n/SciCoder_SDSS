from astropy.io import fits
import numpy as np
import Observation


class Spectrum(Observation):
    def __init__(self):
        super(Spectrum, self).__init__()
        self.flux = None
        self.wavelength = None
        self.plate = None
        self.mjd = None
        self.fibre = None
