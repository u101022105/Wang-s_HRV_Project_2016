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
fname = 'RR_ltdb-14149.txt'
#fname = 'RR_ltdb-14184.txt'
data = np.genfromtxt(fname, delimiter = '')
print('Length of such input data file is : ', len(data))
#print(len(data))
#print(data)
#data = data[1:]
#print(data)
#註解，這裡的ini到end是用在處理過的data上，在e-pend因為數據原始的第0項因為存檔結構的關係為nan所以先去除(可能是eol符號)
#[ini,end] = [0, 18000]



[ini0,end0] = [0, len(data)]
data_op = data[ini0:end0]
#psdp, pdp = mf.PSD(data_op)
#print('The output shape of internal PSDP calcutation : ',np.shape(psdp), ' (for dev checking.)')
#
#apdix = ' data[{:d}:{:d}]'.format(ini,end)
#lbls = ['24hr RR interval'+ apdix, 'Frequency (Hz)', 'PSD', (8,4), 'ind']
#lbls2 = ['LOGLOG 24hr RR interval'+ apdix, 'Log-Frequency', 'Log-PSD', (8,4), 'ind', [-4, -8]]
##mf.DRW(psdp, lbls)
#slope, intercept, r_value, p_value, std_err = mf.DRWLOG(psdp, lbls2)
#print('slope, intercept, r_value, p_value, std_err : \n', slope, intercept, r_value, p_value, std_err)
def SAVE_AS(data, name):
    '''
    saving file as txt, one column, seperated by \n
    '''
    with open(name, 'w') as f:
        for i in range(0, len(data)):
            f.write('{0:.12f}'.format(data[i])+'\n')
    print('Output as '+ name +' successful')
    return 0
def SAVE_AS2(data, name):
    '''
    saving file as txt, one column, seperated by \n
    '''
    with open(name, 'w') as f:
        for i in range(0, len(data[0])):
            f.write('{0:.12f}'.format(data[0][i])+'\t')
            f.write('{0:.12f}'.format(data[1][i])+'\n')
    print('Output as '+ name +' successful')
    return 0
#test8-------------------------------------------------------------------------

lng_dop = len(data_op)
stp_amount = 100
window_width = 10000
stp_len = int(np.round((lng_dop/stp_amount)))
j_itr = [0,10]
[xwu, xwl] = [-4, -8]
[avg_ini, avg_end] = [0, -10]

slplst =[]
inteclst = []
ilst = []
avg_over_lst = []
slp_avglst = []
slp_devilst = []
slp_yrange = [[0, 0]]
window_widthlst  = [] 
print('stp_len :', stp_len)
print('window_width :', window_width)
print('j_itr', j_itr)
print('[xwu, xwl]', [xwu, xwl])
print('[avg_ini, avg_end]', [avg_ini, avg_end])

for j in range(j_itr[0], j_itr[1]):
    j_op = j+1
    curr_win_width = j_op * window_width
    avg_over = np.round(lng_dop/j_op/window_width)
    avg_over_lst = np.append(avg_over_lst, avg_over)
    for i in range(0, stp_amount):
        curr_start = i * stp_len
        [ini,end] = [curr_start , curr_start + curr_win_width]
        data_op_local = data[ini:end]
        psdp, pdp = mf.PSD(data_op_local)
        apdix = ' data[{:d}:{:d}]'.format(ini,end)
        lbls2 = ['LOGLOG 24hr RR interval'+ apdix, 'Log-Frequency', 'Log-PSD', (8,4), 'ind', [xwu, xwl] ]
        slope, intercept, r_value, p_value, std_err = mf.LOGFIT(psdp, lbls2)
        #print('slope, intercept, r_value, p_value, std_err : \n', slope, intercept, r_value, p_value, std_err)
        ilst = np.append( ilst, curr_start)
        slplst = np.append( slplst, slope)
        inteclst = np.append( inteclst, intercept)                              #slplst, ilst, inteclst each contains 'stp_amount' amounts of elements
    devi = np.std(slplst)
    avg = np.average(slplst[avg_ini: avg_end])
    yrange_j = [np.max(slplst)-avg , avg - np.min(slplst)]
    window_widthlst = np.append( window_widthlst, curr_win_width)
    slp_avglst = np.append( slp_avglst, np.average(slplst))                      
    slp_devilst = np.append( slp_devilst, devi)                                  #slp_avglst, slp_devilst each contains 'j_itr' amounts of elements; 
    slp_yrange = np.vstack((slp_yrange, yrange_j))
    print('Under window width of {:d},\nthe average of the slope over these different starting point is : {:.5f} \n\t( Note: the average was taken over slplst[ {:d}: {:d}] .)'.format( curr_win_width, avg, avg_ini, avg_end))
slp_yrange = slp_yrange[1:]

#SAVE_AS(slp_avglst, fname[:-4]+'slope_average.txt')
#SAVE_AS(slp_devilst, fname[:-4]+'slope_deviation.txt')
#SAVE_AS(slp_yrange, fname[:-4]+'slope_yrange.txt')
#SAVE_AS(window_widthlst, fname[:-4]+'window_widthlst.txt')
#SAVE_AS(avg_over_lst, fname[:-4]+'avg_over_amount_lst.txt')
#SAVE_AS2(slp_yrange, fname[:-4]+'slope_yrange2.txt')
#np.savetxt(fname[:-4]+'slope_yrange.csv', slp_yrange, delimiter = ',')
#np.savetxt(fname[:-4]+'slope_yrange.txt', slp_yrange, delimiter = ' ')
'''to plot "slp avg with error bar from deviation" to "window_width" graph'''

#fig8, ax8 = plt.subplots(1,1)
#slope_avg_std, =  ax8.errorbar(window_widthlst, slp_avglst, yerr = slp_devilst, fmt ='ro', ecolor = 'k', capsize = 3, capthick=2)
#slope_avg_line, =ax8.plot(window_widthlst, slp_avglst, label = 'Slope β average')
#slope_avg_dot, = ax8.plot(window_widthlst, slp_avglst, 'r.', label = 'Slope β average')
#ax8.set_title('The "Slope Average" to "Data Window Length" Graph, with Std as error bar'.format(stp_len, stp_len, window_width))
#ax8.set_xlabel('Length of the Window Width (# number), j_op x {:d}'.format(window_width))
#ax8.set_ylabel('"Slope β averaged" value')
#ax8.set_xticks(np.arange(j_itr[0]* window_width, j_itr[1]* window_width, window_width), rotation = 'vertical')
##plt.legend(')
#ax8.legend([slope_avg_dot],['Each point presents the β_avg \nof section [start : start + width], \nwith start = i x {:d} \nand width = j_op x {:d}, j_op = [{:d}...{:d}]'.format( stp_len, window_width, j_itr[0]+1, j_itr[1]+1)],)
#ax8.grid(True)
#plt.show()
#
#fig9, ax9 = plt.subplots(1,1)
#slope_avg_yrange, =  ax9.errorbar(window_widthlst, slp_avglst, yerr = slp_yrange, fmt ='ro', ecolor = 'k', capsize = 3, capthick=2)
#slope_avg_line, = ax9.plot(window_widthlst, slp_avglst, label = 'Slope β average')
#slope_avg_dot, = ax9.plot(window_widthlst, slp_avglst, 'r.', label = 'Slope β average')
#ax9.set_title('The "Slope Average" to "Data Window Length" Graph, with "Slope Dist. Range" as error bar'.format(stp_len, stp_len, window_width))
#ax9.set_xlabel('Length of the Window Width (# number), j_op x {:d}'.format(window_width))
#ax9.set_ylabel('"Slope β averaged" value')
#ax9.set_xticks(np.arange(j_itr[0]* window_width, j_itr[1]* window_width, window_width), rotation = 'vertical')
##plt.legend(')
#ax9.legend([slope_avg_dot],['Each point presents the β_avg \nof section [start : start + width], \nwith start = i x {:d} \nand width = j_op x {:d}, j_op = [{:d}...{:d}]'.format( stp_len, window_width, j_itr[0]+1, j_itr[1]+1)],)
#ax9.grid(True)
#plt.show()

#slp_avglst      = np.genfromtxt(fname[:-4]+'slope_average.txt', delimiter =' ')
#slp_devilst     = np.genfromtxt(fname[:-4]+'slope_deviation.txt', delimiter =' ')
#slp_yrange      = np.genfromtxt(fname[:-4]+'slope_yrange_v2.csv', delimiter =',')
##slp_yrange0     = np.genfromtxt(fname[:-4]+'slope_yrange.txt', delimiter =',', usecols = 0)
##slp_yrange1     = np.genfromtxt(fname[:-4]+'slope_yrange.txt', delimiter =',', usecols = 1)
#window_widthlst = np.genfromtxt(fname[:-4]+'window_widthlst.txt', delimiter =' ')
##print(np.shape(slp_devilst))
#slp_yrange = slp_yrange + np.vstack((slp_avglst,slp_avglst)).T
#slp_yrange = slp_yrange.T 

#fig8, ax8 = plt.subplots(1,1)
##slope_avg_std =  ax8.errorbar(window_widthlst, slp_avglst, yerr = slp_devilst, fmt ='ro', ecolor = 'k', capsize = 3, capthick=2)
#slope_avg_line, = ax8.plot(window_widthlst, slp_avglst, label = 'Slope β average')
#slope_avg_dot, = ax8.plot(window_widthlst, slp_avglst, 'r.', label = 'Slope β average')
#for i, j in zip(window_widthlst, slp_avglst):
#    ax8.annotate(str(np.round(j, 4)), xy = (i , j), rotation = -45)
#ax8.grid(True)
#ax8.set_title('The "Slope Average" to "Data Window Length" Graph'.format(stp_len, stp_len, window_width))
#ax8.set_xlabel('Length of the Window Width (# number), j_op x {:d}'.format(window_width))
#ax8.set_ylabel('"Slope β averaged" value')
#ax8.set_xticks(np.arange(j_itr[0]* window_width, j_itr[1]* window_width, window_width))
#ax8.set_xticklabels(np.arange(j_itr[0]* window_width, j_itr[1]* window_width, window_width), rotation = 'vertical')
#ax8.legend([slope_avg_dot],['Each point presents the β_avg \nof section [start : start + width], \nwith start = i x {:d} \nand width = j_op x {:d}, j_op = [{:d}...{:d}]'.format( stp_len, window_width, j_itr[0]+1, j_itr[1]+1)],bbox_to_anchor=(1.01, 1))
#plt.show()

fig8, ax8 = plt.subplots(1,1)
slope_avg_std =  ax8.errorbar(window_widthlst, slp_avglst, yerr = slp_devilst, fmt ='ro', ecolor = 'k', capsize = 3, capthick=2)
slope_avg_line, = ax8.plot(window_widthlst, slp_avglst, label = 'Slope β average')
slope_avg_dot, = ax8.plot(window_widthlst, slp_avglst, 'r.', label = 'Slope β average')
for i, j in zip(window_widthlst, slp_avglst):
    ax8.annotate(str(np.round(j, 4)), xy = (i , j+ 0.1*j), rotation = -45)
ax8.grid(True)
ax8.set_title('The "Slope Average" to "Data Window Length" Graph, with Std as error bar'.format(stp_len, stp_len, window_width))
ax8.set_xlabel('Length of the Window Width (# number), j_op x {:d}'.format(window_width))
ax8.set_ylabel('"Slope β averaged" value')
ax8.set_xticks(np.arange(j_itr[0]* window_width, j_itr[1]* window_width, window_width))
ax8.set_xticklabels(np.arange(j_itr[0]* window_width, j_itr[1]* window_width, window_width), rotation = 'vertical')
ax8.legend([slope_avg_dot],['Each point presents the β_avg \nof section [start : start + width], \nwith start = i x {:d} \nand width = j_op x {:d}, j_op = [{:d}...{:d}]'.format( stp_len, window_width, j_itr[0]+1, j_itr[1]+1)],bbox_to_anchor=(1.01, 1))
plt.show()

fig9, ax9 = plt.subplots(1,1)
slope_avg_yrange =  ax9.errorbar(window_widthlst, slp_avglst, yerr = slp_yrange, fmt ='ro', ecolor = 'k', capsize = 3, capthick=2)
slope_avg_line, = ax9.plot(window_widthlst, slp_avglst, label = 'Slope β average')
slope_avg_dot, = ax9.plot(window_widthlst, slp_avglst, 'r.', label = 'Slope β average')
ax9.grid(True)
ax9.set_title('The "Slope Average" to "Data Window Length" Graph, with "Slope Dist. Range" as error bar'.format(stp_len, stp_len, window_width))
ax9.set_xlabel('Length of the Window Width (# number), j_op x {:d}'.format(window_width))
ax9.set_ylabel('"Slope β averaged" value')
ax9.set_xticks(np.arange(j_itr[0]* window_width, j_itr[1]* window_width, window_width))
ax9.set_xticklabels(np.arange(j_itr[0]* window_width, j_itr[1]* window_width, window_width), rotation = 'vertical')
ax9.legend([slope_avg_dot],['Each point presents the β_avg \nof section [start : start + width], \nwith start = i x {:d} \nand width = j_op x {:d}, j_op = [{:d}...{:d}]'.format( stp_len, window_width, j_itr[0]+1, j_itr[1]+1)],bbox_to_anchor=(1.01, 1))
plt.show()

fig10, ax10 = plt.subplots(1,1)
slope_avg_yrange =  ax10.errorbar(window_widthlst, slp_avglst, yerr = slp_yrange[0], fmt ='ro', ecolor = 'k', capsize = 3, capthick=2)
slope_avg_line, = ax10.plot(window_widthlst, slp_avglst, label = 'Slope β average')
slope_avg_dot, = ax10.plot(window_widthlst, slp_avglst, 'r.', label = 'Slope β average')
ax10.grid(True)
ax10.set_title('The "Slope Average" to "Data Window Length" Graph, with "Slope Dist. positive Range" as error bar'.format(stp_len, stp_len, window_width))
ax10.set_xlabel('Length of the Window Width (# number), j_op x {:d}'.format(window_width))
ax10.set_ylabel('"Slope β averaged" value')
ax10.set_xticks(np.arange(j_itr[0]* window_width, j_itr[1]* window_width, window_width))
ax10.set_xticklabels(np.arange(j_itr[0]* window_width, j_itr[1]* window_width, window_width), rotation = 'vertical')
ax10.legend([slope_avg_dot],['Each point presents the β_avg \nof section [start : start + width], \nwith start = i x {:d} \nand width = j_op x {:d}, j_op = [{:d}...{:d}]'.format( stp_len, window_width, j_itr[0]+1, j_itr[1]+1)],bbox_to_anchor=(1.01, 1))
plt.show()
print('The last one I used positive range, because the minimum would be very low that it\'s not what we were focusing on.\n See previous work on how the slope saturated over length and how it response to different starting point.')

#print('With X error bar representing the 1/(amount to take into average).')
##test7-------------------------------------------------------------------------
#slplst =[]
#ilst = []
#stp_amount = 100
#window_width = 10000
#stp_len = int(np.round((len(data)/stp_amount)))
#print('stp_len :', stp_len)
#for i in range(0, stp_amount):
#    stp_width = i * stp_len
#    [ini,end] = [stp_width, stp_width+ window_width]
#    apdix = ' data[{:d}:{:d}]'.format(ini,end)
#    lbls2 = ['LOGLOG 24hr RR interval'+ apdix, 'Log-Frequency', 'Log-PSD', (8,4), 'ind', [-4, -8]]
#    data_op = data[ini:end]
#    psdp, pdp = mf.PSD(data_op)
#    slope, intercept, r_value, p_value, std_err = mf.LOGFIT(psdp, lbls2)
##    print('slope, intercept, r_value, p_value, std_err : \n', slope, intercept, r_value, p_value, std_err)
#    ilst = np.append( ilst, stp_width)
#    slplst = np.append( slplst, slope)
#fig7, ax7 = plt.subplots(1,1)
#ax7.plot(ilst, slplst, label = 'Slope β')
#slope_dot, = ax7.plot(ilst, slplst, 'r.', label = 'Slope β')
#ax7.set_title('The slope to data section Graph'.format(stp_len, stp_len, window_width))
#ax7.set_xlabel('position of the starting point, i x {:d}'.format(stp_len))
#ax7.set_ylabel('Slope β value')
##plt.legend(')
#ax7.legend([slope_dot],['Each point presents the β \nof section [start : start + {:d}], with start = i x {:d}'.format( window_width, stp_len)],)
#ax7.grid(True)
#
##plt.ylim((-2, 0))
#plt.show()
#print('The average of the slope over these different initial point is', np.average(slplst[:-10]))


#slplst =[]
#ilst = []
#for i in range(0, 40):
#    [ini,end] = [1000, 2000 + 1000*i]
#    data_op = data[ini:end]
#    psdp, pdp = mf.PSD(data_op)
#    slope, intercept, r_value, p_value, std_err = mf.LOGFIT(psdp, lbls2)
##    print('slope, intercept, r_value, p_value, std_err : \n', slope, intercept, r_value, p_value, std_err)
#    ilst = np.append( ilst, 2000 + 1000*i)
#    slplst = np.append( slplst, slope)
#plt.plot(ilst, slplst)
#plt.title('The slope to data[1000: 2000 + 1000*i] of the data section')
#plt.xlabel('2000 + 1000*i')
#plt.show()
#
#
#
#
#slplst =[]
#ilst = []
#for i in range(0, 40):
#    [ini,end] = [4000, 5000 + 1000*i]
#    data_op = data[ini:end]
#    psdp, pdp = mf.PSD(data_op)
#    slope, intercept, r_value, p_value, std_err = mf.LOGFIT(psdp, lbls2)
##    print('slope, intercept, r_value, p_value, std_err : \n', slope, intercept, r_value, p_value, std_err)
#    ilst = np.append( ilst, 5000 + 1000*i)
#    slplst = np.append( slplst, slope)
#plt.plot(ilst, slplst)
#plt.title('The slope to data[4000: 5000 + 1000*i] of the data section')
#plt.xlabel('5000 + 1000*i')
#plt.show()


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


#test4-------------------------------------------------------------------------
#slplst =[]
#ilst = []
#for i in range(0, 40):
#    [ini,end] = [40000, 41000 + 1000*i]
#    data_op = data[ini:end]
#    psdp, pdp = mf.PSD(data_op)
#    slope, intercept, r_value, p_value, std_err = mf.LOGFIT(psdp, lbls2)
##    print('slope, intercept, r_value, p_value, std_err : \n', slope, intercept, r_value, p_value, std_err)
#    ilst = np.append( ilst, 41000 + 1000*i)
#    slplst = np.append( slplst, slope)
#plt.plot(ilst, slplst)
#plt.title('The slope to data[40000: 41000 + 1000*i] of the data section')
#plt.xlabel('41000 + 1000*i')
#plt.show()

#test5-------------------------------------------------------------------------
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
#plt.plot(ilst, slplst)
#plt.plot(ilst, slplst, 'r.')
#plt.title('The slope to data[i*1000: i*1000+ 10000] section ')
#plt.xlabel('i*1000')
#plt.show()
#print('The average of the slope over these different initial point is', np.average(slplst))

#test6-------------------------------------------------------------------------
#slplst =[]
#ilst = []
#stp_amount = 100
#window_width = 10000
#stp_len = int(np.round((len(data)/stp_amount)))
#print('stp_len :', stp_len)
#for i in range(0, stp_amount):
#    stp_width = i * stp_len
#    [ini,end] = [stp_width, stp_width+ window_width]
#    apdix = ' data[{:d}:{:d}]'.format(ini,end)
#    lbls2 = ['LOGLOG 24hr RR interval'+ apdix, 'Log-Frequency', 'Log-PSD', (8,4), 'ind', [-4, -8]]
#    data_op = data[ini:end]
#    psdp, pdp = mf.PSD(data_op)
#    slope, intercept, r_value, p_value, std_err = mf.LOGFIT(psdp, lbls2)
##    print('slope, intercept, r_value, p_value, std_err : \n', slope, intercept, r_value, p_value, std_err)
#    ilst = np.append( ilst, stp_width)
#    slplst = np.append( slplst, slope)
#plt.plot(ilst, slplst)
#plt.plot(ilst, slplst, 'r.')
#plt.title('The slope to data[i*{:d}: i*{:d}+ {:d}] section '.format(stp_len, stp_len, window_width))
#plt.xlabel('i*{:d}'.format(stp_len))
##plt.ylim((-2, 0))
#plt.show()
#print('The average of the slope over these different initial point is', np.average(slplst[:-10]))



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