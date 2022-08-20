# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 12:02:38 2018

@author: Harry
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import MetroFunc as mf

fname = 'xin-24hr.txt'
data = np.genfromtxt(fname, delimiter = '')
#print(len(data))
#print(data)
data = data[1:]
print(data)



psdp, pdp = mf.PSD(data)
print(np.shape(psdp))

lbls = ['24hr Sync-ElecPendulum', 'Frequency (Hz)', 'PSD', (8,4), 'ind']
lbls2 = ['LOGLOG 24hr Sync-ElecPendulum', 'Log-Frequency', 'Log-PSD', (8,4), 'ind', [-4, -8]]
mf.DRW(psdp, lbls)
slope, intercept, r_value, p_value, std_err = mf.DRWLOG(psdp, lbls2)
print('slope, intercept, r_value, p_value, std_err : \n', slope, intercept, r_value, p_value, std_err)