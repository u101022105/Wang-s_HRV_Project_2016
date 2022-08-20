# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 16:12:47 2018

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

def LOG_SLOPE(data, index, filename):
    '''
    take in data index and filename(no function when doing full iteration over all sections, debug usage when plotting)
    return list of sections' slope value. the slope list was initialized as a list of zeros.
    '''    
    amou_sec = len(index)-1 #how many sections, since every two x coord made one section
    slope_lst = np.zeros((amou_sec))
    x_full = np.arange(1, len(data)+1)
    for i in range(0 , len(index)-1):
    #for i in range(0 , 4):
        sec_ini = int( index[i] )
        sec_end = int( index[i+1] )
        x = x_full[sec_ini : sec_end] - x_full[sec_ini] + 1
        y = data[sec_ini : sec_end]
        b = y[0]
        A = y[-1] #(A在y = y-b+1 之前或之後，目前看來對於最後的結果，可以說是幾乎完全沒影響，至少就斜率a的分布及其值而言沒有影響，R^2值等等是否有被影響，則沒有去仔細探究)
        y = y - b + 1
        x = x/np.max(x)  #(np.max(x) = sec_end' = sec_end - sec_ini)
        #A = y[-1] #(as we knew the x' = 1 is normalized x at x_max, which is x at sec_end, thus y(x'=1) = A happened at y at the last position)
#        print('A=',A)
        y = y/A
        #Then with all new and shifted-normalized x and normalized y 
        lx = np.log(x)
        ly = np.log(y)
        #plt.title('LOGLOG of section {:d} of 14046'.format(i+1) + filename)
        #plt.plot(lx,ly,'-')
        #plt.plot(lx,ly,'r.')
        #plt.show()
        slope, intercept, r_value, p_value, std_err = vr.Fitter(lx,ly, np.min(lx), np.max(lx) )
        slope_lst[i] = slope
    return slope_lst

def LOG_SLOPE2(data, index, filename):
    '''
    take in data index and filename(no function when doing full iteration over all sections, debug usage when plotting)
    return list of sections' slope value. the slope list was initialized as a list of zeros.
    '''    
    amou_sec = len(index)-1 #how many sections, since every two x coord made one section
    slope_lst = np.zeros((amou_sec))
    x_full = np.arange(1, len(data)+1)
    for i in range(0 , len(index)-1):
    #for i in range(0 , 4):
        sec_ini = int( index[i] )
        sec_end = int( index[i+1] )
        x = x_full[sec_ini : sec_end] - x_full[sec_ini] + 1
        y = data[sec_ini : sec_end]
        b = y[0]
        #A = y[-1]
        y = y - b + 1
        x = x/np.max(x)  #(np.max(x) = sec_end' = sec_end - sec_ini)
        A = y[-1] #(as we knew the x' = 1 is normalized x at x_max, which is x at sec_end, thus y(x'=1) = A happened at y at the last position)
        y = y/A #Then with all new and shifted-normalized x and normalized y we took log as follows
        lx = np.log(x)
        ly = np.log(y)
        n = 10
        res, lyinc = hr.smooth1(ly, n)
        lx2 = res[0]
        ly2 = res[1]
        #plt.title('LOGLOG of section {:d} of 14046'.format(i+1) + filename)
        #plt.plot(lx,ly,'-')
        #plt.plot(lx,ly,'r.')
        #plt.show()
        slope, intercept, r_value, p_value, std_err = vr.Fitter(lx2,ly2, np.min(lx2), np.max(lx2) )
        slope_lst[i] = slope
    return slope_lst








def Show_Slope_14046( data, index, filename):
    Slopelst = LOG_SLOPE(data, index, filename)
    fig1, ax1 = plt.subplots(1,1)
    ax1.set_title('The Slope-over-each-section plot')
    ax1.set_xlabel('Sequence of section (#num)')
    ax1.set_ylabel('Slope value')
    ax1.plot(Slopelst,'-')
    ax1.plot(Slopelst,'r.')
    x = np.arange(0,len(Slopelst))
    y = Slopelst
    for i,j in zip(x,y):
        ax1.annotate('({0:.0f} '.format(i) + ', {0:.4f})'.format(j),xy=(i,j))
    fig1.set_size_inches(28, 14)
    ax1.grid(True)
    plt.show()
    return 0
def Show_Slope_14046_2( data, index, filename):
    '''
    This one is with_smoothing_before_fit
    '''
    Slopelst = LOG_SLOPE2(data, index, filename)
    fig1, ax1 = plt.subplots(1,1)
    ax1.set_title('The Slope-over-each-section plot')
    ax1.set_xlabel('Sequence of section (#num)')
    ax1.set_ylabel('Slope value')
    ax1.plot(Slopelst,'-')
    ax1.plot(Slopelst,'r.')
    x = np.arange(0,len(Slopelst))
    y = Slopelst
    for i,j in zip(x,y):
        ax1.annotate('({0:.0f} '.format(i) + ', {0:.4f})'.format(j),xy=(i,j))
    fig1.set_size_inches(14, 7)
    ax1.grid(True)
    plt.show()
    return Slopelst
def Show_Hist_Slope_14046():
    Slopelst = LOG_SLOPE(data, index, filename)
    hst = np.histogram(Slopelst)
    fig2, ax2 = plt.subplots(1,1)
    ax2.set_title('Histogram of Section-Slope of 14046')
    plt.box(True)
    ax2.set_xlabel('Slope value')
    ax2.set_ylabel('Amounts')
    hst2, bin2 , patches = ax2.hist(Slopelst, edgecolor ='black')
    bin_cen = [round((bin2[i]+ bin2[i+1])/2, 5) for i in range(0, len(bin2)-1)]
    ax2.set_xticks(bin_cen)
    fig2.set_size_inches(14, 7)
    plt.show()
    return hst
def Show_Hist_Slope_14046_2():
    Slopelst = LOG_SLOPE2(data, index, filename)
    hst = np.histogram(Slopelst)
    fig2, ax2 = plt.subplots(1,1)
    ax2.set_title('Histogram of Section-Slope of 14046')
    plt.box(True)
    ax2.set_xlabel('Slope value')
    ax2.set_ylabel('Amounts')
    hst2, bin2 , patches = ax2.hist(Slopelst, edgecolor ='black')
    bin_cen = [round((bin2[i]+ bin2[i+1])/2, 5) for i in range(0, len(bin2)-1)]
    ax2.set_xticks(bin_cen)
    #ax2.set_xticklabels(bin_cen)
    fig2.set_size_inches(14, 7)
    plt.show()
    return hst

ind_name = '14046_sec_x_coord.txt'
filename = 'RR_ltdb-14046.txt'
index = np.genfromtxt(ind_name)
data = np.genfromtxt(filename, usecols = 0)

#part1, <f(x)>
#f_avg, count, count2 = F_AVG(data, index)
#plt.plot(count2)
#plt.show()
#plt.plot(f_avg)
#plt.show()
#SAVE_AS(f_avg, '14046_f_avg_1.txt')

#part2, 'a' the power distribution

Slopelst = LOG_SLOPE(data, index, filename)
Show_Slope_14046( data, index, 'RR_ltdb-14046.txt')
Hst = Show_Hist_Slope_14046()

#Slopelst2 = Show_Slope_14046_2( data, index, 'RR_ltdb-14046.txt')
#hst2, bin_edges2 = Show_Hist_Slope_14046_2()


#fig3, ax3 = plt.subplots(1,1)
#hst3, bin3, patches = ax3.hist(Slopelst2, edgecolor = 'black')
#bin_cen = [round((bin3[i]+ bin3[i+1])/2, 5) for i in range(0, len(bin3)-1)]
#ax3.set_xticks(bin_cen)
#ax3.set_xticklabels(bin_cen, rotation ="vertical")
#fig3.set_size_inches(14, 7)
#plt.show()