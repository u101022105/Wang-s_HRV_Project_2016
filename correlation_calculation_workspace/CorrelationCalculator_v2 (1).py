# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 15:14:45 2017

@author: SonicsMacRetina
"""

import numpy as np
from datetime import datetime
version = 'v2.0'
timer = datetime.now()
file = "CC_Itdb_14046.csv"
data = np.genfromtxt(file, delimiter=',')
row2 = data[:,1]
cap= 10000
#cap is to limit the amount of data undergo the calculation in order to shorten the time spent
Tlst = []
#two preparing-phase initialization empty lists
avg = np.average(row2)
print('average of this data file is',avg)
row2 = row2 - avg #make row2 into only the time varience
print('len of data row 2',len(row2), 'capped at', cap)

Tlst = list([sum([row2[n-m]*row2[n] for n in range(m,cap)]) for m in range(0,cap)])

PD = np.abs(np.fft.fft(Tlst))**2

print('shape of fragment list',np.size(Tlst))
np.savetxt(file[:-4]+'_out_'+ str(cap)+'_by_' + str(version)+'.csv', Tlst, delimiter = ',')
np.savetxt('fft_'+file[:-4]+'_out_'+ str(cap)+'_by_' + str(version)+'.csv', PD, delimiter = ',')
print('file output is saved and successful.')
print('duration',datetime.now()-timer)