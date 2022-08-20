# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 14:53:34 2018

@author: SonicsMacRetina
"""
import numpy as np
import HRV_smoothing as hs

#filename = 'RR_U_hbT_ltdb-14046.txt'
filelist = ['RR_ltdb-14046.txt',
'RR_ltdb-14134.txt',
'RR_ltdb-14149.txt',
'RR_ltdb-14157.txt',
'RR_ltdb-14172.txt',
'RR_ltdb-14184.txt']
filename = filelist[0]
data = np.genfromtxt(filename, usecols = 0)
lng = len(data)
#print('The full raw length of this data set is :', lng)
print('length of data = ', lng)
n = 1000
sec_lng = lng/n #把原資料分成n份，每份所需長度為sec_lng
bn = int(np.floor_divide(lng, sec_lng))
#psu_smooth = np.histogram(data, bins = bn) #hist[0] = amount = y; hist[1] = position = x
sm1, inc1 = hs.smooth1(data, n)
[ini,end] = [400,700]
nsm1x = (sm1[0][400:700]-sm1[0][400])/(sm1[0][700]-sm1[0][400])
nsm1y = sm1[1][400:700]/np.max(sm1[1][400:700]) #normalize height
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
tempname = 'Normalized smoothing RR-t, from '+str(end)+' segments, \nfile = '+ filename + ' cut into {:d} sections'.format(n)
hs.draw([nsm1x, nsm1y, np.log(inc1)], tempname, 5)
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
seq2 = [[-6.2,-0.2],[-4.3,-0.15],[-4.3,-0.15],[-3.6,-0.21],[-3.5,-0.22],[-3.0,-0.10],[-3.1,-0.10],[-1.5,-0.17],[-1.4,-0.20],[-1.0,-0.04],[-1.1,-0.10],[-0.5,-0.24],[-0.4,-0.22],[0,-0.10]]
psu_data2 = hs.gen4(seq2, [1000,1000])
hs.draw([psu_data2[0], psu_data2[1], '1'],'Gen4 generated data', 5)
#hs.draw([np.log(psu_data2[0]),np.log( psu_data2[1]), '1'],'test', 5)
#with open('Pseudo_ltdb14046_RR_Sth1000_400_700_1000_Gen4.txt', 'w') as f:
#    x = psu_data2[0]
#    y = psu_data2[1]
#    res = np.transpose(np.vstack([y,x]))
#    temp = [f.write(str(res[i])[2:-2]+'\n') for i in range(0, len(res))]