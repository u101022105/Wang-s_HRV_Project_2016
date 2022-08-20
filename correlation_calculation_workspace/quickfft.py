# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 13:00:38 2017

@author: Harry
"""
"""this is a quick fft machine"""
import numpy as np
from datetime import datetime
timer = datetime.now()
timer = datetime.now()
file = "CC_Itdb_14046.csv"
data = np.genfromtxt(file, delimiter=',')
row2 = data[:,1]
cap= 8000
ff = np.abs(np.fft.fft(row2[0:cap]))
np.savetxt('fft'+ file[7:-4]+ "_capped_" + str(cap) + '.csv', ff, delimiter = ',')
print('file output is saved and successful.')
print('duration',datetime.now()-timer)