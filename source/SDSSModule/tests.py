from Observation import *
filename = '/Users/pranavtalwar/SampleProject/data/spec-4055-55359-0001.fits'
hdu_list = fits.open(filename)
hdu1 = hdu_list[0]

print(f"This file has {len(hdu_list)} HDUs.")