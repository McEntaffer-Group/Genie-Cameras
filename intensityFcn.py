import numpy as np


def sincSqdFcn(x, x_0, D, I_0):
    return I_0*np.sinc(((x-x_0)*np.pi*375*5.86)/(0.4065*D))**2


def gaussFcn(y, y_0, sigma, a):
    return a*np.exp(-(y-y_0)**2/(2*sigma**2))


def intensityFcn(sinc, gauss):
    return sinc*gauss
