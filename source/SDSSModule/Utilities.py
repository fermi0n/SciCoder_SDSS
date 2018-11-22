from Observation import *
def spectra_plot(self):

        plt.figure()
        plt.plot(self.wavelength, self.flux, linewidth=0.4)
        plt.grid(linewidth=0.4, linestyle='--', alpha=0.6)
        x1 = self.wavelength[0]
        x2 = self.wavelength[len(self.wavelength) - 1]
        plt.xlim([x1, x2])
        plt.xlabel(r'Wavelength [$\AA$]')
        plt.ylabel('Flux [F$_{\lambda}$]')
        plt.title(self.spectrum_name)

        plt.show()

filename = input("Enter a file:")
spectrum = Observation(filename)

spectra_plot(spectrum)