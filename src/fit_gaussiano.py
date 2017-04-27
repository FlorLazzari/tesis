# para fitear con una gaussiana
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def fitear_gaussiana(x,y):
    # valores iniciales:
    mean = sum(x*y)
    sigma = sum(y*(x - mean)**2)

    # por que esto no funciona?!?

    # def gauss_function(x, a, x0, sigma, c):
    #     return ((a*np.exp(-(x-x0)**2/(2*sigma**2))) - c)

    # Define model function to be used to fit to the data above:

    def gauss_function(x, a, x0, sigma):
        return a*np.exp(-(x-x0)**2/(2*sigma**2))

    # p0 is the initial guess for the fitting coefficients (A, mu and sigma above)
    popt, pcov = curve_fit(gauss_function, x, y, p0 = [1, mean, sigma]) #, 0.1])  el -0.1 lo puse a dedo del grafico

    # plot data
    plt.plot(x, y,'x')
    # Get the fitted curve
    plt.plot(x, gauss_function(x, *popt), label='fit')
    plt.legend()
    # plt.title('')
    plt.xlabel(r'$y / d_{0}$')
    plt.ylabel(r'$ \Delta U / U_{\infty} $')
    plt.show()
    # Finally, lets get the fitting parameters, i.e. the mean and standard deviation:
    sigma = popt[2]
    return sigma
