# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 14:37:49 2018

@author: Harry
"""

import numpy as np
import matplotlib.pyplot as plt
import FTABSQ_viewer_for_smoothing_test_re as vr


fname_x = '14046_sec_x_coord.txt'
fname_s = 'Slope_of_RR_ltdb-14046_for_op.csv'
xc_data = np.genfromtxt(fname_x, delimiter = ' ')
slp_data = np.genfromtxt(fname_s, delimiter = ',')

#version 5 varied x length-------------------
[plen, elelen] = [12500, 2500]
x = np.arange(1,plen+1)
#xlst = [elelen+ 2000 , elelen +1000,  elelen-1000,  elelen,  elelen-2000]
xlst = [elelen,elelen,elelen,elelen,elelen]
y = [60/72]
#xlst = [3000, 1000, 2500, 3500]
#xlst = [2500, 2500, 2500, 2500]
for i in range(0, len(Alst)):
    x1 = (np.arange(1, xlst[i]+1))/xlst[i]
    y_elem = Alst[i]* x1 ** alpha[i]
    if alpha[i] < 0 :
        y_elem = y_elem - (np.min(y_elem))  + 60/72
    elif alpha[i] > 0 :
        y_elem = y_elem - (np.max(y_elem))  + 60/72
    for j in range(0, xlst[i]):
        y = np.append(y, y_elem[j])
y = y[1:]