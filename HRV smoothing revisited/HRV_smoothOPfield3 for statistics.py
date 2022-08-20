# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 21:32:38 2018

@author: Harry
In order to do statistics by roughly putting every 4000 points into one section, and perform statistics on it to see
if mean <f(x)> is something similar to 1/x^a .
"""

import numpy as np
import HRV_smoothing2 as hs
import matplotlib.pyplot as plt
import scipy.stats as st
import FTABSQ_viewer_for_smoothing_test_re as vr

#filename = 'RR_U_hbT_ltdb-14046.txt'
filelist = ['RR_ltdb-14046.txt',
'RR_ltdb-14134.txt',
'RR_ltdb-14149.txt',
'RR_ltdb-14157.txt',
'RR_ltdb-14172.txt',
'RR_ltdb-14184.txt']
filename = filelist[0]
nor = 0                                                                         #option for data normalization before plotting.
n = 1000                                                                        #how many sections I want the raw data to be smoothed into 
[ini,end] = [0,n]                                                            #data start and end cut
xlbl = 'Sequence of RR (#num)'                                                  #xlabel
ylbl = 'Duration of RR (second)'                                                #ylabel
show_coord = 0                                                                  #display coordinates on plot , ==1 show, else don't show
lbl = [xlbl, ylbl, show_coord]

data = np.genfromtxt(filename, usecols = 0)
lng = len(data)
sec_lng = lng/n                                                                 #把原資料分成n份，每份所需長度為sec_lng
#bn = int(np.floor_divide(lng, sec_lng))
#psu_smooth = np.histogram(data, bins = bn) #hist[0] = amount = y; hist[1] = position = x
sm1, inc1 = hs.smooth1(data, n)
#print('The full raw length of this data set is :', lng)
print('length of data = ', lng)



if nor == 1:
    nsm1x = (sm1[0][ini:end]-sm1[0][ini])/(sm1[0][end]-sm1[0][ini])             #normalized length
    nsm1y = sm1[1][ini:end]/np.max(sm1[1][ini:end])                             #normalized height
elif nor == 2:
    nsm1x = sm1[0][ini:end]                                                     # raw length, absolute x coor
    nsm1y = sm1[1][ini:end]/np.max(sm1[1][ini:end])                             #normalized height
elif nor == 0:
    nsm1x = sm1[0][ini:end]                                                     # raw length, absolute x coor
    nsm1y = sm1[1][ini:end]                                                     # raw height, absolute y coor
    
#__________________________doing statistics____________________________________

raw_sec = 5000 #raw_section is how many points is one section of 趨勢 for the data, this is roughly set by me, currently it's about 4000-6000 by my eyes and performed a rough statistics by me. 
f = np.zeros((raw_sec))

i = 0
while (i+1) * raw_sec < lng :
    f = f + data[ i*raw_sec : (i+1)*raw_sec]
    i = (i + 1)
f = f/(i-1) #(因為最後一個i= i' 循環被截止，所以取平均十的分母i = i'-1)
plt.plot(f)
plt.show()
#plt.plot(data[0: raw_sec])
#plt.show()
nor2 = 0
n2= 1000
sec_lng2 = raw_sec/n2
[ini2,end2] = [0,n2]  
sm2, inc2 = hs.smooth1(f, n2)
xlbl2 = 'Sequence of RR (#num)'                                                  #xlabel
ylbl2 = 'Duration of RR (second)'                                                #ylabel
show_coord2 = 0                                                                  #display coordinates on plot , ==1 show, else don't show
show_tks = 0
lbl2 = [xlbl2, ylbl2, show_coord2, show_tks ]

if nor2 == 1:
    nsm2x = (sm2[0][ini2:end2]-sm2[0][ini2])/(sm2[0][end2]-sm2[0][ini2])             #normalized length
    nsm2y = sm2[1][ini2:end2]/np.max(sm2[1][ini2:end2])                             #normalized height
elif nor2 == 2:
    nsm2x = sm2[0][ini2:end2]                                                    # raw length, absolute x coor
    nsm2y = sm2[1][ini2:end2]/np.max(sm2[1][ini2:end2])                             #normalized height
elif nor2 == 0:
    nsm2x = sm2[0][ini2:end2]                                                     # raw length, absolute x coor
    nsm2y = sm2[1][ini2:end2]                                                     # raw height, absolute y coor    
#tempname2 = 'Smoothing Averaged RR-t, from Average of every '+str(raw_sec)+' points as a segment, \nfile = '+ filename + ' data length: {:d}'.format(lng) +' and cut into {:d} sections'.format(n2) +'\n Each section was a smoothing of {0:.0f} raw data points'.format(round(sec_lng2))
#hs.draw([nsm2x, nsm2y, np.log(inc2)], tempname2, 5 , lbl2)
lx2, ly2 = np.log(nsm2x), np.log(nsm2y)
tempname2 = 'LOGLOG Smoothing Averaged RR-t, from Average of every '+str(raw_sec)+' points as a segment, \nfile = '+ filename + ' data length: {:d}'.format(lng) +' and cut into {:d} sections'.format(n2) +'\n Each section was a smoothing of {0:.0f} raw data points'.format(round(sec_lng2))
hs.draw([lx2, ly2, np.log(inc2)], tempname2, 5 , lbl2)
slope, intercept, r_value, p_value, std_err = vr.Fitter(lx2,ly2, 4, 6 )
print(slope, intercept, r_value, p_value, std_err)

#___________________________Drawing raw and smoothed data___________________________
#draw(data, 'Raw RR-t, file = '+ filename, 0)
#draw([sm1[0], sm1[1],inc1], '1st attempt of smoothing RR-t, file = '+ filename + ' cut into {:d} sections'.format(n), 1)
    #hs.draw([sm1[0][ini:end], sm1[1][ini:end], inc1], '1st attempt of smoothing RR-t, showing first '+str(end)+' segments, file = '+ filename + ' cut into {:d} sections'.format(n), 1)
    ###print('sm1 x, y [0:10]',[sm1[0][0:10], sm1[1][0:10]])
    ##sm1lx = [np.log(sm1[0][i]) for i in range(ini, end)]
    ##sm1ly = [np.log(sm1[1][i]) for i in range(ini, end)]
    ##tempname = 'loglog smoothing RR-t, showing first '+str(end)+' segments, file = '+ filename + ' cut into {:d} sections'.format(n)
    ##draw([sm1lx, sm1ly, np.log(inc1)], tempname, 4)
    #

'''normalized y in this 400,700 section'''
'''
#tempname = 'Normalized smoothing RR-t, from '+str(end)+' segments, \nfile = '+ filename + ' data length: {:d}'.format(lng) +' cut into {:d} sections'.format(n) +'\n Each section was a smoothing of {0:.0f} raw data points'.format(round(sec_lng))
tempname = 'Smoothing RR-t, from '+str(end)+' segments, \nfile = '+ filename + ' data length: {:d}'.format(lng) +' cut into {:d} sections'.format(n) +'\n Each section was a smoothing of {0:.0f} raw data points'.format(round(sec_lng))
hs.draw([nsm1x, nsm1y, np.log(inc1)], tempname, 5 , lbl)
'''


#'''loglog version normalized y in this 400,700 section'''
#nsm1lx = [np.log(nsm1x) for i in range(ini, end)]
#nsm1ly = [np.log(nsm1y) for i in range(ini, end)]
#tempname = 'loglog normalized smoothing RR-t, from '+str(end)+' segments, \nfile = '+ filename + ' cut into {:d} sections'.format(n)
#hs.draw([nsm1lx, nsm1ly, np.log(inc1)], tempname, 5)


#---------------------------Drawing raw and smoothed data---------------------------

#___________________________Generating x y from model of smoothed data___________________________
#seq = [[4.660,-0.158],[4.685,	-0.095],[4.685,	-0.120],[4.730,	-0.140],[4.731,	-0.140],[4.790,	-0.070],[4.791,	-0.135],[4.830,	-0.160],[4.831,	-0.160],[4.885,	-0.110],[4.890,	-0.140],[4.910,	-0.105]]
##psu_data = gen(seq, [10,10])
##psu_data2 = gen2(seq, [1000,1000])
#psu_data2_2 = hs.gen3(seq, [1000,1000])
'''
seq2 = [[-6.2,-0.2],[-4.3,-0.15],[-4.3,-0.15],[-3.6,-0.21],[-3.5,-0.22],[-3.0,-0.10],[-3.1,-0.10],[-1.5,-0.17],[-1.4,-0.20],[-1.0,-0.04],[-1.1,-0.10],[-0.5,-0.24],[-0.4,-0.22],[0,-0.10]]
psu_data2 = hs.gen4(seq2, [1000,1000])
hs.draw([psu_data2[0], psu_data2[1], '1'],'Gen4 generated data', 5)
'''
#hs.draw([np.log(psu_data2[0]),np.log( psu_data2[1]), '1'],'test', 5)
#with open('Pseudo_ltdb14046_RR_Sth1000_400_700_1000_Gen4.txt', 'w') as f:
#    x = psu_data2[0]
#    y = psu_data2[1]
#    res = np.transpose(np.vstack([y,x]))
#    temp = [f.write(str(res[i])[2:-2]+'\n') for i in range(0, len(res))]