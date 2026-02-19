# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 15:25:15 2021

@author: Keir Hunter
"""

import numpy as np
from skimage import measure


def findIntensity(array):
    # creating boolean array
    thresh_arr = array>25
    # finding areas above threshhold value
    labels = measure.label(thresh_arr)
    # creating regions of interest
    props = measure.regionprops(labels, array)
    
    # looping through each area of interest and summing intensity
    intensity = 0
    for i in props:
        intensity += i.mean_intensity
        
    return intensity
    
