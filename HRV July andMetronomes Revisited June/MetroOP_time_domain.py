# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 12:02:38 2018

@author: Harry
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import MetroFunc as mf
import HRV_smoothing2_forEP as hs

fname = 'xin-24hr.txt'
data = np.genfromtxt(fname, delimiter = '')
data = data[1:]
print(data)
nor = 0                                                                         #option for data normalization before plotting.
n = 250                                                                        #how many sections I want the raw data to be smoothed into 
[ini,end] = [0,n]   




lbls = ['24hr Sync-ElecPendulum Time domain', 'Sequence (# num)', 'Period (sec)', (16,8), 'ind']
xd = np.arange(0, len(data[0:1000]))
mf.DRW((xd,data[0:1000]), lbls)

sm1, inc1 = hs.smooth1(data, n)
if nor == 1:
    nsm1x = (sm1[0][ini:end]-sm1[0][ini])/(sm1[0][end]-sm1[0][ini])             #normalized length
    nsm1y = sm1[1][ini:end]/np.max(sm1[1][ini:end])                             #normalized height
elif nor == 2:
    nsm1x = sm1[0][ini:end]                                                     # raw length, absolute x coor
    nsm1y = sm1[1][ini:end]/np.max(sm1[1][ini:end])                             #normalized height
elif nor == 0:
    nsm1x = sm1[0][ini:end]                                                     # raw length, absolute x coor
    nsm1y = sm1[1][ini:end]                                                     # raw height, absolute y coor

lng = len(data)
sec_lng = lng/n    
show_coord = 0
tempname = 'Normalized smoothing Sync-EPend, from '+str(end)+' segments, \nfile = '+ fname + ' data length: {:d}'.format(lng) +' cut into {:d} sections'.format(n) +'\n Each section was a smoothing of {0:.0f} raw data points'.format(round(sec_lng))
lbl = [lbls[1], lbls[2], show_coord, 1]
hs.draw([nsm1x, nsm1y, np.log(inc1)], tempname, 5 , lbl)



#psdp, pdp = mf.PSD(data)
#print(np.shape(psdp))
#lbls = ['24hr Sync-ElecPendulum', 'Frequency (Hz)', 'PSD', (8,4), 'ind']
#lbls2 = ['LOGLOG 24hr Sync-ElecPendulum', 'Log-Frequency', 'Log-PSD', (8,4), 'ind', [-4, -8]]
#mf.DRW(psdp, lbls)
#slope, intercept, r_value, p_value, std_err = mf.DRWLOG(psdp, lbls2)
#print('slope, intercept, r_value, p_value, std_err : \n', slope, intercept, r_value, p_value, std_err)