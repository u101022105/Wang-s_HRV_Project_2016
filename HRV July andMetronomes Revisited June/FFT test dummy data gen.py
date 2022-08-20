# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 15:57:51 2018

@author: Harry
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import MetroFunc as mf

#x = np.arange(0, 100000)
#y = np.sin(x)
#
#np.savetxt('fft dummy input.csv', y, delimiter =',')

data = np.genfromtxt('fft dummy input.csv', delimiter =',')
ft = np.fft.fft(data)
#print(ft[1])
np.savetxt('fft dummy output FFT full 冠珵.csv', np.vstack((ft.real, ft.imag)).T, fmt='%.18g',delimiter =',')
#pd = np.abs(ft)**2
#lng = len(pd)
#hlf = int(np.round(lng/2))
#xd = np.arange(0, hlf)+1
#psd = pd[:hlf]/np.max( pd[:hlf])
#xsd = xd/ np.max(xd)
#psdp = np.vstack((xsd,psd))
#
##np.savetxt('dummy ft output.csv', pd, delimiter =',')
#lbls = ['LOGLOG Dummy input', 'Log-Frequency', 'Log-PSD', (8,4), 'ind', [-4, -8]]
#mf.DRWLOG(psdp,lbls)