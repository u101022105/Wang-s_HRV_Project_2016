# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 12:02:38 2018

@author: Harry
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import MetroFunc as mf

#fname = 'RR_ltdb-14046.txt'
fname = 'xin-24hr.txt'
data = np.genfromtxt(fname, delimiter = '')
print(len(data))
#print(len(data))
#print(data)
data = data[1:]
#print(data)
#註解，這裡的ini到end是用在處理過的data上，在e-pend因為數據原始的第0項因為存檔結構的關係為nan所以先去除(可能是eol符號)
[ini,end] = [0, len(data)]
data_op = data[ini:end]
psdp, pdp = mf.PSD(data_op)
print(np.shape(psdp))

apdix = ' data[{:d}:{:d}]'.format(ini,end)
lbls = ['24hr RR interval'+ apdix, 'Frequency (Hz)', 'PSD', (8,4), 'ind']
lbls2 = ['LOGLOG 24hr RR interval'+ apdix, 'Log-Frequency', 'Log-PSD', (8,4), 'ind', [-4, -8]]
#mf.DRW(psdp, lbls)
slope, intercept, r_value, p_value, std_err = mf.DRWLOG(psdp, lbls2)
print('slope, intercept, r_value, p_value, std_err : \n', slope, intercept, r_value, p_value, std_err)
#test1-------------------------------------------------------------------------
slplst =[]
ilst = []
for i in range(0, 40):
    [ini,end] = [1000, 2000 + 1000*i]
    data_op = data[ini:end]
    psdp, pdp = mf.PSD(data_op)
    slope, intercept, r_value, p_value, std_err = mf.LOGFIT(psdp, lbls2)
#    print('slope, intercept, r_value, p_value, std_err : \n', slope, intercept, r_value, p_value, std_err)
    ilst = np.append( ilst, 2000 + 1000*i)
    slplst = np.append( slplst, slope)
plt.plot(ilst, slplst)
plt.plot(ilst, slplst,'r.')
plt.title('The slope to data[1000: 2000 + 1000*i] of the data section')
plt.xlabel('2000 + 1000*i')
plt.grid(True)
plt.show()
#test2-------------------------------------------------------------------------
slplst =[]
ilst = []
for i in range(0, 40):
    [ini,end] = [4000, 5000 + 1000*i]
    data_op = data[ini:end]
    psdp, pdp = mf.PSD(data_op)
    slope, intercept, r_value, p_value, std_err = mf.LOGFIT(psdp, lbls2)
#    print('slope, intercept, r_value, p_value, std_err : \n', slope, intercept, r_value, p_value, std_err)
    ilst = np.append( ilst, 5000 + 1000*i)
    slplst = np.append( slplst, slope)
plt.plot(ilst, slplst)
plt.plot(ilst, slplst,'r.')
plt.title('The slope to data[4000: 5000 + 1000*i] of the data section')
plt.xlabel('5000 + 1000*i')
plt.grid(True)
plt.show()
#test4-------------------------------------------------------------------------
slplst =[]
ilst = []
for i in range(0, 40):
    [ini,end] = [40000, 41000 + 1000*i]
    data_op = data[ini:end]
    psdp, pdp = mf.PSD(data_op)
    slope, intercept, r_value, p_value, std_err = mf.LOGFIT(psdp, lbls2)
#    print('slope, intercept, r_value, p_value, std_err : \n', slope, intercept, r_value, p_value, std_err)
    ilst = np.append( ilst, 41000 + 1000*i)
    slplst = np.append( slplst, slope)
plt.plot(ilst, slplst)
plt.plot(ilst, slplst,'r.')
plt.title('The slope to data[40000: 41000 + 1000*i] of the data section')
plt.xlabel('41000 + 1000*i')
plt.grid(True)
plt.show()

#test3-------------------------------------------------------------------------
#slplst =[]
#ilst = []
#for i in range(0, 60):
#    [ini,end] = [i*1000, i*1000+ 10000]
#    apdix = ' data[{:d}:{:d}]'.format(ini,end)
#    lbls2 = ['LOGLOG 24hr RR interval'+ apdix, 'Log-Frequency', 'Log-PSD', (8,4), 'ind', [-4, -8]]
#    data_op = data[ini:end]
#    psdp, pdp = mf.PSD(data_op)
#    slope, intercept, r_value, p_value, std_err = mf.DRWLOG(psdp, lbls2)
##    print('slope, intercept, r_value, p_value, std_err : \n', slope, intercept, r_value, p_value, std_err)
#    ilst = np.append( ilst, i*1000)
#    slplst = np.append( slplst, slope)
#plt.plot(ilst, slplst)
#plt.title('The slope to data[i*1000: i*1000+ 10000] section ')
#plt.xlabel('i*1000')
#plt.show()
#
#[ini,end] = [40000, 50000]
#data_op = data[ini:end]
#psdp, pdp = mf.PSD(data_op)
##print(np.shape(psdp))
#apdix = ' data[{:d}:{:d}]'.format(ini,end)
#lbls = ['24hr RR interval'+ apdix, 'Frequency (Hz)', 'PSD', (8,4), 'ind']
#lbls2 = ['LOGLOG 24hr RR interval'+ apdix, 'Log-Frequency', 'Log-PSD', (8,4), 'ind', [-4, -8]]
##mf.DRW(psdp, lbls)
#slope, intercept, r_value, p_value, std_err = mf.DRWLOG(psdp, lbls2)
#print('slope, intercept, r_value, p_value, std_err : \n', slope, intercept, r_value, p_value, std_err)
#-----------------------------------------------------------------------------
##test3.5-------------------------------------------------------------------------
#slplst =[]
#ilst = []
#for i in range(0, 60):
#    [ini,end] = [i*1000, i*1000+ 10000]
#    apdix = ' data[{:d}:{:d}]'.format(ini,end)
#    lbls2 = ['LOGLOG 24hr RR interval'+ apdix, 'Log-Frequency', 'Log-PSD', (8,4), 'ind', [-4, -8]]
#    data_op = data[ini:end]
#    psdp, pdp = mf.PSD(data_op)
#    slope, intercept, r_value, p_value, std_err = mf.LOGFIT(psdp, lbls2)
##    print('slope, intercept, r_value, p_value, std_err : \n', slope, intercept, r_value, p_value, std_err)
#    ilst = np.append( ilst, i*1000)
#    slplst = np.append( slplst, slope)
#plt.plot(ilst, slplst)
#plt.title('The slope to data[i*1000: i*1000+ 10000] section ')
#plt.xlabel('i*1000')
#plt.show()
#
#[ini,end] = [40000, 50000]
#data_op = data[ini:end]
#psdp, pdp = mf.PSD(data_op)
##print(np.shape(psdp))
#apdix = ' data[{:d}:{:d}]'.format(ini,end)
#lbls = ['24hr RR interval'+ apdix, 'Frequency (Hz)', 'PSD', (8,4), 'ind']
#lbls2 = ['LOGLOG 24hr RR interval'+ apdix, 'Log-Frequency', 'Log-PSD', (8,4), 'ind', [-4, -8]]
##mf.DRW(psdp, lbls)
#slope, intercept, r_value, p_value, std_err = mf.DRWLOG(psdp, lbls2)
#print('slope, intercept, r_value, p_value, std_err : \n', slope, intercept, r_value, p_value, std_err)
##-----------------------------------------------------------------------------
#
#
#
##test5-------------------------------------------------------------------------
#slplst =[]
#ilst = []
#for i in range(0, 95):
#    [ini,end] = [i*1000, i*1000+ 10000]
#    apdix = ' data[{:d}:{:d}]'.format(ini,end)
#    lbls2 = ['LOGLOG 24hr RR interval'+ apdix, 'Log-Frequency', 'Log-PSD', (8,4), 'ind', [-4, -8]]
#    data_op = data[ini:end]
#    psdp, pdp = mf.PSD(data_op)
#    slope, intercept, r_value, p_value, std_err = mf.LOGFIT(psdp, lbls2)
##    print('slope, intercept, r_value, p_value, std_err : \n', slope, intercept, r_value, p_value, std_err)
#    ilst = np.append( ilst, i*1000)
#    slplst = np.append( slplst, slope)
#fig5, ax5 = plt.subplots(1,1)
#ax5.plot(ilst, slplst)
#ax5.set_title('The slope to data[i*1000: i*1000+ 10000] section ')
#ax5.set_xlabel('i*1000')
#ax5.set_xticks(np.arange(0, 94*1000+ 10000, 5000))
#ax5.set_xticklabels(np.arange(0, 94*1000+ 10000, 5000), rotation ='vertical')
#plt.show()
#print('The average of the slope over these different initial point is', np.average(slplst))
#
##test5.5-------------------------------------------------------------------------
#slplst =[]
#ilst = []
#for i in range(0, 100):
#    [ini,end] = [i*1000, i*1000+ 10000]
#    apdix = ' data[{:d}:{:d}]'.format(ini,end)
#    lbls2 = ['LOGLOG 24hr RR interval'+ apdix, 'Log-Frequency', 'Log-PSD', (8,4), 'ind', [-4, -8]]
#    data_op = data[ini:end]
#    psdp, pdp = mf.PSD(data_op)
#    slope, intercept, r_value, p_value, std_err = mf.LOGFIT(psdp, lbls2)
##    print('slope, intercept, r_value, p_value, std_err : \n', slope, intercept, r_value, p_value, std_err)
#    ilst = np.append( ilst, i*1000)
#    slplst = np.append( slplst, slope)
#fig5, ax5 = plt.subplots(1,1)
#ax5.plot(ilst, slplst)
#ax5.set_title('The slope to data[i*1000: i*1000+ 10000] section ')
#ax5.set_xlabel('i*1000')
#ax5.set_xticks(np.arange(0, 100*1000+ 10000, 5000))
#ax5.set_xticklabels(np.arange(0, 100*1000+ 10000, 5000), rotation ='vertical')
#plt.show()
#print('The average of the slope over these different initial point is', np.average(slplst))
#
##test6-------------------------------------------------------------------------
#slplst =[]
#ilst = []
#for i in range(0, 10):
#    [ini,end] = [i*10000, i*10000+ 10000]
#    apdix = ' data[{:d}:{:d}]'.format(ini,end)
#    lbls2 = ['LOGLOG 24hr RR interval'+ apdix, 'Log-Frequency', 'Log-PSD', (8,4), 'ind', [-4, -8]]
#    data_op = data[ini:end]
#    psdp, pdp = mf.PSD(data_op)
#    slope, intercept, r_value, p_value, std_err = mf.LOGFIT(psdp, lbls2)
##    print('slope, intercept, r_value, p_value, std_err : \n', slope, intercept, r_value, p_value, std_err)
#    ilst = np.append( ilst, i*10000)
#    slplst = np.append( slplst, slope)
#plt.plot(ilst, slplst)
#plt.title('The slope to data[i*10000: i*10000+ 10000] section ')
#plt.xlabel('i*10000')
#plt.show()
#print('The average of the slope over these different initial point is', np.average(slplst))

#with open(fname[:-4] + 'psdp.txt', 'w') as f:
#    for i in range(0, len(psdp[1])):
#        f.write(str(psdp[1][i]))
#        f.write('\n')
#
#with open(fname[:-4] + 'LOG10psdp.txt', 'w') as f:
#    for i in range(0, len(psdp[1])):
#        f.write(str(np.log10(psdp[1][i])))
#        f.write('\n')
#        
#with open(fname[:-4] + 'NATURALLOGpsdp.txt', 'w') as f:
#    for i in range(0, len(psdp[1])):
#        f.write(str(np.log(psdp[1][i])))
#        f.write('\n')