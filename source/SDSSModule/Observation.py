from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

# class Spectrum (Observation):

#   def __init__(self):
#       self.flux = None
#       self.wavelength = None
#       self.plate = None
#       self.mjd = None
#       self.fibre = None

class Observation(object):

    def __init__(self, filename):
        self._spectrum_name = None
        self.ra = None  # will be a float
        self.dec = None  # will be a float
        self.redshift = None  # will be a float
        self.timestamp = None  # will be a timestamp
        # self.spectrum = None    #will be a Spectrum object
        self.plate = None
        self.mjd = None
        self.fiber = None
        self.flux = None  # numpy arrays of length X
        self.wavelength = None  # numpy arrays of length X (same as above)

        # Load fits file, called filename
        # load into the above variables

        with fits.open(filename) as hdulist:
            meta = hdulist[0]  # This is where ra, dec, plate, mjd, fiber is in
            spectrum = hdulist[1].data  # This is where flux and wavelength is in
            line_info = hdulist[3].data  # Contains multiple redshift measurements for different emission lines
            # Average over measured redshifts
            self.redshift = np.mean([j for j in [i[5] for i in line_info] if j != 0])
            # Extract ra and etc
            self.ra = meta.header['RA']
            self.dec = meta.header['DEC']
            self.plate = meta.header['PLATEID']
            self.mjd = meta.header['MJD']
            self.fiber = meta.header['FIBERID']
            # Extract wavelength and flux, note the 10**
            self.wavelength = np.asarray([10 ** i[1] for i in spectrum])
            self.flux = np.asarray([i[0] for i in spectrum])

    def testing(self):
        print(self.wavelength)
        print(self.redshift)

    # This method allows printing the spectrum name as
    # plate-mjd-xxxx
    # This allows easy integration with the sdss online browser service
    # as well as conversion into urls
    @property
    def spectrum_name(self):
        if self._spectrum_name is None:
            fiber_string = str(self.fiber)
            while len(str(fiber_string)) != 4:
                fiber_string = '0' + fiber_string
            self._spectrum_name = str(self.plate) + '-' + str(self.mjd) + '-' + fiber_string
        return self._spectrum_name

    def spectra_plot(self):

        plt.figure()
        plt.plot(self.wavelength,self.flux, linewidth = 0.4)
        plt.grid(linewidth = 0.4, linestyle='--', alpha = 0.6)
        x1 = self.wavelength[0]
        x2 = self.wavelength[len(self.wavelength)-1]
        plt.xlim([x1,x2])
        plt.xlabel(r'Wavelength []$\AA$]')
        plt.ylabel('Flux [F$_{\lambda}$]')
        plt.title(self.name)


        plt.show()
