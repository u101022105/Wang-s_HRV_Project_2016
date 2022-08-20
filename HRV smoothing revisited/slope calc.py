# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 18:42:20 2018

@author: Harry
"""
import numpy as np
seq = [[4.660,-0.158],[4.685,	-0.095],[4.685,	-0.120],[4.730,	-0.140],[4.731,	-0.140],[4.790,	-0.070],[4.791,	-0.135],[4.830,	-0.160],[4.831,	-0.160],[4.885,	-0.110],[4.890,	-0.140],[4.910,	-0.105]]
i= 0
mlst =[]
while i < 12:
    m = ((seq[i+1][1]-seq[i][1])/(seq[i+1][0]-seq[i][0]))
    mlst = np.append(mlst, m)
    i  = i+2
print(mlst)

#with open('slope_test.txt', 'w') as f:
#    for i in range(0, len(mlst)):
#        f.write(str(mlst[i])+'\n')