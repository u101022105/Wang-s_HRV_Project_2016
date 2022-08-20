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

(sizex, sizey) = (20, 10)
fname = 'xin-24hr.txt'
#fname = 'positive_period of rec0019_160.txt'
#fname = 'positive_period of rec0023_160.txt'
#fname = 'positive_period of rec0024_160.txt'
#fname = '1219_168_2_ori.txt'
#fname = '0213_168_1_ori.txt'
data = np.genfromtxt(fname, delimiter = '')
data = data[1:]
print(data)
print(len(data))
nor = 0                                                                         #option for data normalization before plotting.
n = 150                                                                       #how many sections I want the raw data to be smoothed into 
[ini,end] = [0,n]   




#lbls = ['24hr Sync-ElecPendulum Time domain', 'Sequence (# num)', 'Period (sec)', (16,8), 'ind']

lbls = ['Sync-ed Metronome Time domain \n from'+ fname[:-4] , 'Sequence (# num)', 'Period (sec)', (sizex, sizey), 'ind']

#Plotting Raw==================================================================
#dummy = 0
#xd = np.arange(0, len(data[0:1000]))
##mf.DRW((xd,data[0:1000]), lbls)
#show_coord = 0
#lbl0 = [lbls[1], lbls[2], show_coord, 1, 10, 0.001, [sizex, sizey]]
#hs.draw([xd,data[0:1000], dummy], lbls[0], 5 , lbl0)



#Smoothing=====================================================================
#sm1, inc1 = hs.smooth1(data, n)
#if nor == 1:
#    nsm1x = (sm1[0][ini:end]-sm1[0][ini])/(sm1[0][end]-sm1[0][ini])             #normalized length
#    nsm1y = sm1[1][ini:end]/np.max(sm1[1][ini:end])                             #normalized height
#elif nor == 2:
#    nsm1x = sm1[0][ini:end]                                                     # raw length, absolute x coor
#    nsm1y = sm1[1][ini:end]/np.max(sm1[1][ini:end])                             #normalized height
#elif nor == 0:
#    nsm1x = sm1[0][ini:end]                                                     # raw length, absolute x coor
#    nsm1y = sm1[1][ini:end]                                                     # raw height, absolute y coor
#
#lng = len(data)
#sec_lng = lng/n
#xstep = sec_lng    
#show_coord = 0
#tempname = 'Normalized Smoothed Sync-ed Metronome Time domain, from '+str(end)+' segments, \nfile = '+ fname + ' data length: {:d}'.format(lng) +' cut into {:d} sections'.format(n) +'\n Each section was a smoothing of {0:.0f} raw data points'.format(round(sec_lng))
#lbl = [lbls[1], lbls[2], show_coord, 1, xstep, 0.0001, [sizex, sizey]]
#hs.draw([nsm1x, nsm1y, np.log(inc1)], tempname, 5 , lbl)

#Frequency Domain==============================================================
(sizex, sizey) = (10,5)
xrng = [-4, -8]
data_for_psd = data[2000:-10000]
psdp, pdp = mf.PSD(data_for_psd)
print(np.shape(psdp))
lbls = ['Sync-ed 24hr ElecPendulum Frequency domain \n from'+ fname[:-4] , 'Frequency (Hz)', 'PSD', (sizex, sizey), 'ind']
lbls2 = ['LOGLOG Sync-ed 24hr ElecPendulum Frequency domain \n from'+ fname[:-4] , 'Log-Frequency', 'Log-PSD', (sizex, sizey), 'ind', xrng]
#mf.DRW(psdp, lbls)
slope, intercept, r_value, p_value, std_err = mf.DRWLOG(psdp, lbls2)
print('slope, intercept, r_value, p_value, std_err : \n', slope, intercept, r_value, p_value, std_err)


#(sizex, sizey) = (10,5)
#xrng = [-4, -8]
#for i in range(0, 5):
#    if i == 0:
#        data_for_psd = data[1000:]
#    else:
#        data_for_psd = data[1000:-1000*i]
#    psdp, pdp = mf.PSD(data_for_psd)
#    print(np.shape(psdp))
#    lbls = ['Sync-ed Metronome Frequency domain \n from '+ fname[:-4] , 'Frequency (Hz)', 'PSD', (sizex, sizey), 'ind']
#    lbls2 = ['LOGLOG Sync-ed Metronome Frequency domain \n from '+ fname[:-4] , 'Log-Frequency', 'Log-PSD', (sizex, sizey), 'ind', xrng]
#    #mf.DRW(psdp, lbls)
#    slope, intercept, r_value, p_value, std_err = mf.DRWLOG(psdp, lbls2)
#    #print('data[ {:d}: end]'.format(1000*i))
#    print('data[ 1000: -{:d}]'.format(1000*i))
#    print('slope, intercept, r_value, p_value, std_err : \n', slope, intercept, r_value, p_value, std_err)
#    print('\n')

#psdp, pdp = mf.PSD(data)
#print(np.shape(psdp))
#lbls = ['24hr Sync-ElecPendulum', 'Frequency (Hz)', 'PSD', (8,4), 'ind']
#lbls2 = ['LOGLOG 24hr Sync-ElecPendulum', 'Log-Frequency', 'Log-PSD', (8,4), 'ind', [-4, -8]]
#mf.DRW(psdp, lbls)
#slope, intercept, r_value, p_value, std_err = mf.DRWLOG(psdp, lbls2)
#print('slope, intercept, r_value, p_value, std_err : \n', slope, intercept, r_value, p_value, std_err)