import numpy as np
import scipy.optimize
from intensityFcn import gaussFcn


def gaussCurvefit(y, z, guess):
    popt, pcov = scipy.optimize.curve_fit(gaussFcn, y, z, p0=guess)
    return popt
