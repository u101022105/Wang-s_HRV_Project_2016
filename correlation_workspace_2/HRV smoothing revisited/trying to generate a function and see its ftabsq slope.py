# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 18:47:54 2018

@author: Harry
"""

import numpy as np
import matplotlib.pyplot as plt
import FTABSQ_viewer_for_smoothing_test_re as vr

x= np.arange(1,10001)
y = x**(-0.008)
ft = np.fft.fft(y)
pd = np.abs(ft)**2


#lx = np.log(np.arange(1,len(pd)+1))
#ly = np.log(pd)
#plt.plot(lx, ly)
#plt.show()
#
#lx = np.log(np.arange(1,len(pd)+1))[:5001]
#ly = np.log(pd)[:5001]
#plt.plot(lx, ly)
#plt.show()

#lx = np.log(np.arange(1,len(pd)+1))[1:5001]
#ly = np.log(pd)[1:5001]


Alst =[11 , 8 , 7 , 6]
A1, A2, A3, A4 = Alst/np.sum(Alst)
x= np.arange(1,10001)
y = A1* x**(-0.008) + A2* x**(+0.00128) + A3* x**(+0.01010) + A4* x**(-0.01635)
ft = np.fft.fft(y)
pd = np.abs(ft)**2

x = np.arange(1,len(pd)+1)[1:5001]
y = pd[1:5001]
x = x/np.max(x)
y = y/np.max(y)

lx = np.log(x)
ly = np.log(y)
slope, intercept, r_value, p_value, std_err = vr.Fitter(lx, ly, -7, -3)
psu_y = lx*slope + intercept
plt.plot(lx, ly)
plt.plot(lx, psu_y,'r--')
plt.title('LOGLOG of Generated data with f(x) = A1 x ^(-0.008) + A2 x^(+0.00128) + A3 x^(+0.01010)+  A4 x^(-0.01635)')
plt.ylabel('Log(PSD)')
plt.xlabel('Log(sequence)')
plt.show()

print('slope, intercept', slope, intercept)
print('A1 to A4 :',[11 , 8 , 7 , 6])