# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 19:20:25 2018

@author: Harry
"""

import numpy as np
import matplotlib.pyplot as plt
import HRV_smoothing2 as hr
import FTABSQ_viewer_for_smoothing_test_re as vr

def F_AVG(data, index):
    '''
    take in raw data and the index for sections
    return chopped(for statistics validity)-f_avg (sections-avg) 
    and the count of how many times the data points accumulated during the addition operation, 
    and count2 as the chopped-count array.
    '''
    max_dis = int(np.max(index[1:]- index[:-1]))
    f = np.zeros((max_dis))
    count = np.zeros((max_dis))
    for i in range(0,len(index)-1):
        sec_ini = int( index[i] )
        sec_end = int( index[i+1] )
        sec_dis = int( sec_end - sec_ini )
        residue_lng = max_dis - sec_dis
        temp = data[sec_ini : sec_end]
        temp2 = np.ones((sec_dis))
        f = f + np.append( temp, np.zeros((residue_lng)))
        count = count + np.append( temp2, np.zeros((residue_lng)))
    j = 0
    while j < len(count):  #in order to avoid non-statistical valid things, like if something only happened once in the whole dataset
        if count[j] <= 1.0:
            count2 = count[0:j]
            new_len = j
            j = j + len(count) #break loop
        else:
            j = j+1
    f_avg = np.divide(f[0:new_len], count2)
    print('The statistical valid least-time the addition happened allowed \n is(otherwise chopped and disgarded) : {:d}'.format(int(count2[-1])))
    return [f_avg, count, count2]

def SAVE_AS(data, name):
    '''
    saving file as txt, one column, seperated by \n
    '''
    with open(name, 'w') as f:
        for i in range(0, len(data)):
            f.write('{0:.12f}'.format(data[i])+'\n')
    print('Output as '+ name +' successful')
    return 0

#ind_name = '14046_sec_x_coord.txt'
#filename = 'RR_ltdb-14046.txt'
#index = np.genfromtxt(ind_name)
#data = np.genfromtxt(filename, usecols = 0)
#part1, <f(x)>
#f_avg, count, count2 = F_AVG(data, index)
#plt.plot(count2)
#plt.show()
#plt.plot(f_avg)
#plt.show()
#SAVE_AS(f_avg, '14046_f_avg_1.txt')
filename2 = '14046_f_avg_1.txt'
data2 = np.genfromtxt(filename2, usecols = 0)
y = data2
x = np.arange(1, len(y)+1)
b = y[0]
A = y[-1] #(as we knew the x' = 1 is normalized x at x_max, which is x at sec_end, thus y(x'=1) = A happened at y at the last position)
y = y - b + 1
x = x/np.max(x)  #(np.max(x) = sec_end' = sec_end - sec_ini)
y = y/A #Then with all new and shifted-normalized x and normalized y we took log as follows
ly = np.log(y)
lx = np.log(x)


slope, intercept, r_value, p_value, std_err = vr.Fitter(lx, ly, -7, -3)
fig, ax = plt.subplots(1,1)
ax.plot(lx,ly)
ax.set_title('LOGLOG <f(x)> to x plot, and the fitting of its time domain slope below')
plt.show()
print('slope, intercept', slope, intercept)


#slope = -0.00191
#slope1 = slope
#x = np.arange(1,10001)
#y = intercept**slope * x**(slope)
#x = x/ np.max(x)
##y = y/ np.max(y)
#pd = np.abs(np.fft.fft(y))**2
#lpd = np.log(pd)[1:5001]
#lx = np.log(x)[1:5001]
#slope, intercept, r_value, p_value, std_err = vr.Fitter(lx, lpd, -7, -3)
#fig1,ax1 = plt.subplots(1,1)
#ax1.plot(lx, lpd)
#ax1.plot(lx, lx*slope + intercept, 'r--')
#ax1.set_title('LOGLOG PSD of the model generated y = A x^({0:.5f}) data'.format(slope1))
#plt.show()
#print('slope, intercept', slope, intercept)

slope = -0.00191
slope1 = slope
x = np.arange(1,10001)
y = intercept**slope * x**(slope)
x = x/ np.max(x)
#y = y/ np.max(y)
pd = np.abs(np.fft.fft(y))**2
lpd = np.log(pd)[1:5001]
lx = np.log(x)[1:5001]
slope, intercept, r_value, p_value, std_err = vr.Fitter(lx, lpd, -7, -3)
fig1,ax1 = plt.subplots(1,1)
ax1.plot(lx, lpd)
ax1.plot(lx, lx*slope + intercept, 'r--')
ax1.set_title('LOGLOG PSD of the model generated y = A x^({0:.5f}) data'.format(slope1))
plt.show()
print('slope, intercept', slope, intercept)


