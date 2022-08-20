# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 13:15:14 2017

@author: SonicsMacRetina
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 12:46:03 2017

@author: SonicsMacRetina
"""

import numpy as np
from datetime import datetime
timer = datetime.now()
file = "CC_Itdb_14046.csv"
data = np.genfromtxt(file, delimiter=',')
row2 = data[:,1]
cap= 10000
#cap is to limit the amount of data undergo the calculation in order to shorten the time spent
Tlst = []
#two preparing-phase initialization empty lists
print('len of data row 2',len(row2), 'capped at', cap)

Tlst = list([sum([row2[n-m]*row2[n] for n in range(m,cap)]) for m in range(0,cap)])

PD = np.abs(np.fft.fft(Tlst))**2

print('shape of fragment list',np.size(Tlst))
np.savetxt(file[:-4]+'_out_'+ str(cap)+'_by_v1.2.csv', Tlst, delimiter = ',')
np.savetxt('fft_'+file[:-4]+'_out'+ str(cap)+'_by_v1.2.csv', PD, delimiter = ',')
print('file output is saved and successful.')
print('duration',datetime.now()-timer)