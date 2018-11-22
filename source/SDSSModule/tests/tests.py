from ..Observation import *
import numpy as np
filename = 'spec-4055-55359-0001.fits'
hdu_list = fits.open(filename)
hdu1 = hdu_list[0]

print(f"This file has {len(hdu_list)} HDUs.")

def test_spectrum_read():
	#Check if the spectrum is actually opened
	assert len(hdu_list) == 4, "Unexpected number of HDUs, please check your file!"

spectrum = Observation(filename)

def test_flux():
	#Check if a certain wavelength corresponds to the correct flux.
	wavelength = spectrum.wavelength
	flux = spectrum.flux
	assert len(flux) == len(wavelength), "Mismatching flux and wavelength size, reconfirm extraction!"

def test_ra():
	#Check if the ra is actually the ra of the spectrum.
	ra = spectrum.ra
	np.testing.assert_approx_equal(ra,236.4332)

def test_dec():
	#Check if the dec is actually the dec of the spectrum.
	dec = spectrum.dec
	np.testing.assert_approx_equal(dec,1.836429)

#To get the values of plate,mjd and fiber
splitting_the_filename = filename.split('-')
plate = splitting_the_filename[1]
mjd = splitting_the_filename[2]
#stripping the index 3 is necessary to remove '.fits'
fiber = splitting_the_filename[3].strip('.fits')

def test_plate():
	plate = spectrum.plate
	assert plate == 4055, "The file doesn't have the correct plate number"

def test_mjd():
	mjd = spectrum.mjd
	assert mjd == 55359, "The file doesn't have the correct mjd number"

def test_fiber():
	fiber = spectrum.fiber
	assert fiber == 1, "The file doesn't have the correct fiber number"

def test_method_spectrum_name():
	spectrum_name = spectrum.spectrum_name
	assert spectrum_name == '{}-{}-{}'.format(plate,mjd,fiber), "method Spectrum name is not working,recheck"

