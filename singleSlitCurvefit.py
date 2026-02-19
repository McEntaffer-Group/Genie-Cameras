import numpy as np
import scipy.optimize
from intensityFcn import sincSqdFcn


def singleSlitCurvefit(x, z, guess):
    popt, pcov = scipy.optimize.curve_fit(sincSqdFcn, x, z, p0=guess)
    return popt
