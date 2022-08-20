# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 12:46:03 2017

@author: SonicsMacRetina
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:22:53 2017

@author: Harry
"""
import numpy as np
from datetime import datetime
timer = datetime.now()
file = "CC_Itdb_14046.csv"
data = np.genfromtxt(file, delimiter=',')
row2 = data[:,1]
cap= 40000
#cap is to limit the amount of data undergo the calculation in order to shorten the time spent
#tmp = []
tmp = 0
Tlst = []
#two preparing-phase initialization empty lists
print('len of data row 2',len(row2), 'capped at', cap)

for m in range(0,cap):
    for n in range(m,cap):
        tmp = tmp + row2[n-m]*row2[n]
    Tlst=np.append(Tlst,tmp)
    tmp = 0
#        print(tmp,n,m)
#        if n >= m:
#            print('ba',tmp) #examining code
#            tmp = tmp+row2[n-m]*row2[n]
#            print('af',tmp) #examining code
#            tmp = np.append(tmp,row2[n-m]*row2[n])   #frag= fragment to be summed
#    Tlst=np.append(Tlst,np.sum(tmp))
#    tmp = 0
#    tmp = []  # reinitialize the tmp list after one T[m] is calculated
    
print('shape of fragment list',np.shape(Tlst))
np.savetxt(file[:-4]+'_out_by_v1.15.csv', Tlst, delimiter = ',')
print('file output is saved and successful.')
print('duration',datetime.now()-timer)