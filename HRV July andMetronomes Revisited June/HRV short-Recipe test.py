# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 13:44:04 2018

@author: SonicsMacRetina
"""

import numpy as np
import matplotlib.pyplot as plt
import GeneralPSDFunc as gp

fname = 'RR_ltdb-14046.txt'
data = np.genfromtxt(fname, delimiter =' ')
lng = len(data)



def FitSOP(data, cond, opt):
    '''
    cond = [ini, lng_cut ]
    '''
    [ini, look_after ] = cond
    end = ini + look_after
    data_part = data[ini: end ]
    psdp, pdp = gp.PSD(data_part)
    lbls1 =['DLOG [ {:d} : {:d} ] Length 14046 PSD'.format(ini, end), 'NLOG Frequency', 'NLOG Magnitude', (8,4), 'ind', [-4,-8]]
    fithdl = gp.LOGFIT(psdp, lbls1)
    slope, intercept, r_value, p_value, std_err = fithdl
    rsq = r_value**2
    if opt == 1:
        print('\n')
        print('Full Length divided by {:d}'.format(i))
        print('Test Length is : {:d}'.format(look_after))
        print('{:d} Length Beta Value = {:.5f}, R2 = {:.3f}'.format(look_after ,slope, r_value**2))
    return slope, rsq
    
#{FULL LENGTH BETA}
def Full_len(data):
    psdp, pdp = gp.PSD(data)
    lbls1 =['DLOG Full Length 14046 PSD', 'NLOG Frequency', 'NLOG Magnitude', (8,4), 'ind', [-4,-8]]
    fithdl = gp.DRWLOG(psdp, lbls1)
    slope, intercept, r_value, p_value, std_err = fithdl
    print('\n')
    print('Full Length \nBeta Value :{:>10.5f}\nR2 : {:>16.3f}'.format(slope, r_value**2))
    return 0
def Full_len_noplot(data):
    psdp, pdp = gp.PSD(data)
    lbls1 =['DLOG Full Length 14046 PSD', 'NLOG Frequency', 'NLOG Magnitude', (8,4), 'ind', [-4,-8]]
    fithdl = gp.LOGFIT(psdp, lbls1)
    slope, intercept, r_value, p_value, std_err = fithdl
    print('Full Length \nBeta Value :{:>10.5f}\nR2 : {:>16.3f}'.format(slope, r_value**2))
    return 0
#Full_len_noplot(data)

  
#{THE 1st RECIPE TEST} 
dash = '-'*40   
Slope_lst = []
i = 1
lng_cut = int(np.round(lng/i))
ini = 0
itr = 1000
look_after = 40000
j = 0
while (j*itr + ini + look_after) <  lng_cut:
    cond = [j*itr+ ini, look_after]
    slope, r2 = FitSOP(data, cond, 0)
    Slope_lst = np.append(slope, Slope_lst)
    j = j+1
avg = np.average(Slope_lst[:-1])

beta_from_full = -0.81216
tdr = Slope_lst
#plt.title('The Beta-Sequence Plot, \nwithout the last Beta in Slope List')
plt.title('The Beta-Sequence Plot')
x = np.arange(1, len(tdr)+1)
plt.plot(x,tdr,'-*g',label = 'Slope List')
plt.plot(np.ones(len(tdr)+1)*avg, '-r', label = 'Averaged Value')
plt.plot(np.ones(len(tdr)+1)*beta_from_full, '--b', label = 'Full-Len Beta Value')
plt.ylabel('Beta Value')
plt.xlabel('Slope list')
plt.xticks(x)
plt.xlim((1,len(tdr)))
plt.grid(True)
plt.legend()
plt.show()

print(dash)
print('Full Data length :{:>20d}'.format(lng))
print(dash)
print('Current Set Slices   :       {:>10s}'.format('1/' + str(i)))
print('Current Length Limit :       {:>10d}'.format(lng_cut))
print('Current ini          :       {:>10d}'.format(ini))
print('Current iterating stepwidth :{:>10d}'.format(itr))
print('Current look_after length   :{:>10d}'.format(look_after))
print('Iterated times: {:>22d}'.format(j-1))
print(dash)
print('Avg of Slope in Cut-Length : {:>10.5f}'.format(avg))
print('(Without the last fit, contains defects)')
print(dash)
print('Targeted Results:')
print('Beta Value :                 {:>10s}'.format('-0.81216'))
print(dash)
#Full_len_noplot(data)

















#{LEGACY CODE}
#{PART of LENGTH BETA}
#ini = 1000
#for i in range(2, 11):
#    lng_cut = int( np.round(lng/i))
#    data_part = data[ini: lng_cut ]
#    psdp, pdp = gp.PSD(data_part)
#    lbls1 =['DLOG [ {:d} : {:d} ] Length 14046 PSD'.format(ini, lng_cut), 'NLOG Frequency', 'NLOG Magnitude', (8,4), 'ind', [-4,-8]]
#    fithdl = gp.DRWLOG(psdp, lbls1)
#    slope, intercept, r_value, p_value, std_err = fithdl
#    print('\n')
#    print('Full Length divided by {:d}'.format(i))
#    print('Test Length is : {:d}'.format(lng_cut))
#    print('{:d} Length Beta Value = {:.5f}, R2 = {:.3f}'.format(lng_cut - ini,slope, r_value**2))
  