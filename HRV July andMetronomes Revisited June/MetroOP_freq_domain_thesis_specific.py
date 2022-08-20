# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 12:02:38 2018

@author: Harry
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import MetroFunc_specific as mf

fname = 'xin-24hr.txt'
#fname = 'xin-24hr_single.txt'
data = np.genfromtxt(fname, delimiter = '')
#print(len(data))
#print(data)
data = data[1:]
#data = data - np.average(data)  #variablility
print(data)

psdp, pdp = mf.PSD(data)
print(np.shape(psdp))
#xwl = 0.04
#xwu = 0.0033
lxwl = np.log10(0.04)
lxwu = np.log10(0.0001)

lbls = ['24hr Synced-Electric Metronomes', 'Frequency (Hz)', 'PSD', (6,4), 'ind']
lbls2 = ['Double-Log-Plot of 24hr Synced-Electric Metronomes', 'Log(Frequency)', 'Log(Relative Power)', (6,4), 'ind', [lxwl, lxwu]]
#lbls2 = ['LOGLOG 24hr Sync-ElecPendulum', 'Log-Frequency', 'Log-PSD', (8,4), 'ind', [-4, -8]]

#lbls = ['24hr Single-Electric Metronomes', 'Frequency (Hz)', 'PSD', (6,4), 'ind']
#lbls2 = ['Double-Log-Plot of 24hr Single-Electric Metronomes', 'Log(Frequency)', 'Log(Relative Power)', (6,4), 'ind', [lxwl, lxwu]]
#lbls2 = ['LOGLOG 24hr Sync-ElecPendulum', 'Log-Frequency', 'Log-PSD', (8,4), 'ind', [-4, -8]]
#mf.DRW(psdp, lbls)
slope, intercept, r_value, p_value, std_err = mf.DRWLOG(psdp, lbls2)
print('slope, intercept, r_value, p_value, std_err : \n', slope, intercept, r_value, p_value, std_err)

#with open(fname[:-4] + 'psdp.txt', 'w') as f:
#    for i in range(0, len(psdp[1])):
#        f.write(str(psdp[1][i]))
#        f.write('\n')
#
#with open(fname[:-4] + 'LOG10psdp.txt', 'w') as f:
#    for i in range(0, len(psdp[1])):
#        f.write(str(np.log10(psdp[1][i])))
#        f.write('\n')
#        
#with open(fname[:-4] + 'NATURALLOGpsdp.txt', 'w') as f:
#    for i in range(0, len(psdp[1])):
#        f.write(str(np.log(psdp[1][i])))
#        f.write('\n')