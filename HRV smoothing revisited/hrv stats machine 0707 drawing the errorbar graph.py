# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 16:12:47 2018

@author: Harry
"""

import numpy as np
import matplotlib.pyplot as plt
import HRV_smoothing3 as hr
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
"""
#temporarily archived at 0705 5:44pm, 
#before really implement the 'm' function
def LOG_SLOPE2(data, index, filename, n, m):
    '''
    take in data index and filename(no function when doing full iteration over all sections, debug usage when plotting)
    return list of sections' slope value. the slope list was initialized as a list of zeros.
    '''    
    '''
    n for smooth, m for experimental, to neglect the last m points in fitting loglog slope.
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
        #lx = np.log(x)
        ly = np.log(y)
        #n = 10
        res, lyinc = hr.smooth1(ly, n, 0)
        lx_tmp = res[0]
        lx2 = np.log((lx_tmp)/np.max(lx_tmp))
        ly2 = res[1]
        plt.title('LOGLOG of section {:d} of 14046'.format(i+1) + filename)
        plt.plot(lx2,ly2,'-')
        plt.plot(lx2,ly2,'r.')
        
        slope, intercept, r_value, p_value, std_err = vr.Fitter(lx2,ly2, np.min(lx2), np.max(lx2) )
        ly_psu = lx2 * slope + intercept
        plt.plot(lx2,ly_psu,'k-')
        plt.annotate('y = {:.2f} x + {:.2f}'.format(slope, intercept), xy = ((np.max(lx2)+np.min(lx2))/2, (np.max(ly2)+np.min(ly2))/2), xytext =((np.max(lx2)+np.min(lx2))/2, (np.max(ly2)+np.min(ly2))/2))
        plt.show()
        slope_lst[i] = slope
    return slope_lst
"""

def LOG_SLOPE2(data, index, filename, n, m, drw):
    '''
    take in data index and filename(no function when doing full iteration over all sections, debug usage when plotting)
    return list of sections' slope value. the slope list was initialized as a list of zeros.
    '''    
    '''
    n for smooth, m for experimental, to neglect the last m points in fitting loglog slope.
    '''
    amou_sec = len(index)-1 #how many sections, since every two x coord made one section
    slope_lst = np.zeros((amou_sec))
    x_full = np.arange(1, len(data)+1)
    m1, m2 = int(m[0]), int(m[1])
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
        #lx = np.log(x)
        ly = np.log(y)
        #n = 10
        res, lyinc = hr.smooth1(ly, n, 0)
        lx_tmp = res[0]+1
        lx2 = np.log((lx_tmp)/np.max(lx_tmp))
        ly2 = res[1]
        if drw == 1:
            plt.title('LOGLOG of section {:d} of 14046'.format(i+1) + filename)
            plt.plot(lx2,ly2,'-')
            plt.plot(lx2,ly2,'r.')
            slope, intercept, r_value, p_value, std_err = vr.Fitter(lx2,ly2, np.min(lx2[m1:-m2]), np.max(lx2[m1:-m2]) )
            ly_psu = lx2 * slope + intercept
            plt.plot(lx2,ly_psu,'k-')
            plt.annotate('y = {:.2f} x + {:.2f}'.format(slope, intercept), xy = ((np.max(lx2)+np.min(lx2))/2, (np.max(ly2)+np.min(ly2))/2), xytext =((np.max(lx2)+np.min(lx2))/2, (np.max(ly2)+np.min(ly2))/2))
            plt.axvspan(np.min(lx2[m1:-m2]), np.max(lx2[m1:-m2]), color='grey', alpha=0.5)
            plt.show()
        else:
            slope, intercept, r_value, p_value, std_err = vr.Fitter(lx2,ly2, np.min(lx2[m1:-m2]), np.max(lx2[m1:-m2]) )
        slope_lst[i] = slope
    return slope_lst

def Show_Slope_14046_2( data, index, filename, n_for_smooth, m_to_neglect, drw):
    '''
    This one is with_smoothing_before_fit
    '''
    Slopelst = LOG_SLOPE2(data, index, filename, n_for_smooth, m_to_neglect, drw)
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


def Show_Hist_Slope_14046_2(n_for_smooth, m_to_neglect, drw):
    #n_for_smooth = 100
    Slopelst = LOG_SLOPE2(data, index, filename, n_for_smooth, m_to_neglect, drw)
    hst = np.histogram(Slopelst)
    fig2, ax2 = plt.subplots(1,1)
    ax2.set_title('Histogram of Section-Slope of 14046')
    plt.box(True)
    ax2.grid(True)
    ax2.set_xlabel('Slope value')
    ax2.set_ylabel('Amounts')
    hst2, bin2 , patches = ax2.hist(Slopelst, edgecolor ='black')
    #bin_cen = [round((bin2[i]+ bin2[i+1])/2, 5) for i in range(0, len(bin2)-1)]
    bin_cen = [(bin2[i]+ bin2[i+1])/2 for i in range(0, len(bin2)-1)]
    #bin_rep = bin2[:-1]
    bin_rep = bin_cen
    ax2.set_xticks(bin_rep)
    #ax2.set_xticklabels(bin_cen)
    fig2.set_size_inches(14, 7)
    plt.show()
    posi = np.sum([hst2[i] for i in range(0, len(bin_rep)) if bin_rep[i] >= 0])
    nega = np.sum([hst2[i] for i in range(0, len(bin_rep)) if bin_rep[i] < 0])
    print('+ :',posi,'- :',nega)
    return hst


##################################################################################################################
#########################################################  OPERATION FIELD  ######################################
##################################################################################################################
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
#Slopelst = LOG_SLOPE(data, index, filename)
n_for_smooth = 100
m_to_neglect = [1,20]
drw = 0
#Slopelst = LOG_SLOPE2(data, index, filename, n_for_smooth)
Slopelst2 = Show_Slope_14046_2( data, index, 'RR_ltdb-14046.txt', n_for_smooth, m_to_neglect, drw)
Hst = Show_Hist_Slope_14046_2(n_for_smooth, m_to_neglect, drw)
##############################################################################
#####################  SAVING FILES  #########################################
##############################################################################
#np.savetxt('Slope of '+ filename[:-4] + '.csv', Slopelst2, delimiter = ',', header = 'Slope of '+ filename[:-4] + '\n and its n_for_smooth and m_to_neglect are {:.12f} [{:.1f} to -{:.1f}]'.format(n_for_smooth, m_to_neglect[0], m_to_neglect[1]))

#np.savetxt()
#np.savetxt('SlopeHst of '+ filename[:-4] + '.csv', Hst, delimiter = ',')

#Slopelst2 = Show_Slope_14046_2( data, index, 'RR_ltdb-14046.txt')
#hst2, bin_edges2 = Show_Hist_Slope_14046_2()


#fig3, ax3 = plt.subplots(1,1)
#hst3, bin3, patches = ax3.hist(Slopelst2, edgecolor = 'black')
#bin_cen = [round((bin3[i]+ bin3[i+1])/2, 5) for i in range(0, len(bin3)-1)]
#ax3.set_xticks(bin_cen)
#ax3.set_xticklabels(bin_cen, rotation ="vertical")
#fig3.set_size_inches(14, 7)
#plt.show()







##################################################################################################################
###############################################  TEMP DISCARDED CODE LINES  ######################################
##################################################################################################################
#def Show_Slope_14046( data, index, filename):
#    Slopelst = LOG_SLOPE(data, index, filename)
#    fig1, ax1 = plt.subplots(1,1)
#    ax1.set_title('The Slope-over-each-section plot')
#    ax1.set_xlabel('Sequence of section (#num)')
#    ax1.set_ylabel('Slope value')
#    ax1.plot(Slopelst,'-')
#    ax1.plot(Slopelst,'r.')
#    x = np.arange(0,len(Slopelst))
#    y = Slopelst
#    for i,j in zip(x,y):
#        ax1.annotate('({0:.0f} '.format(i) + ', {0:.4f})'.format(j),xy=(i,j))
#    fig1.set_size_inches(28, 14)
#    ax1.grid(True)
#    plt.show()
#    return 0
#def Show_Hist_Slope_14046():
#    Slopelst = LOG_SLOPE(data, index, filename)
#    hst = np.histogram(Slopelst)
#    fig2, ax2 = plt.subplots(1,1)
#    ax2.set_title('Histogram of Section-Slope of 14046')
#    plt.box(True)
#    ax2.set_xlabel('Slope value')
#    ax2.set_ylabel('Amounts')
#    hst2, bin2 , patches = ax2.hist(Slopelst, edgecolor ='black')
#    bin_cen = [round((bin2[i]+ bin2[i+1])/2, 5) for i in range(0, len(bin2)-1)]
#    ax2.set_xticks(bin_cen)
#    fig2.set_size_inches(14, 7)
#    plt.show()
#    return hst
#def LOG_SLOPE22(data, index, filename):
#    '''
#    take in data index and filename(no function when doing full iteration over all sections, debug usage when plotting)
#    return list of sections' slope value. the slope list was initialized as a list of zeros.
#    '''    
#    amou_sec = len(index)-1 #how many sections, since every two x coord made one section
#    slope_lst = np.zeros((amou_sec))
#    x_full = np.arange(1, len(data)+1)
#    for i in range(0 , len(index)-1):
#    #for i in range(0 , 4):
#        sec_ini = int( index[i] )
#        sec_end = int( index[i+1] )
#        x = x_full[sec_ini : sec_end] - x_full[sec_ini] + 1
#        y = data[sec_ini : sec_end]
#        n = 10
#        res, lyinc = hr.smooth1(y, n,0)
#        x2 = res[0]
#        y2 = res[1]
#        b = y2[0]
#        #A = y[-1]
#        y2 = y2 - b + 1
#        x2 = x2/np.max(x2)  #(np.max(x) = sec_end' = sec_end - sec_ini)
#        A = y2[-1] #(as we knew the x' = 1 is normalized x at x_max, which is x at sec_end, thus y(x'=1) = A happened at y at the last position)
#        y2 = y2/A #Then with all new and shifted-normalized x and normalized y we took log as follows
#        #lx = np.log(x)
#        #ly = np.log(y)
#        lx2 = np.log(x2)
#        ly2 = np.log(y2)
#        #plt.title('LOGLOG of section {:d} of 14046'.format(i+1) + filename)
#        #plt.plot(lx,ly,'-')
#        #plt.plot(lx,ly,'r.')
#        #plt.show()
#        slope, intercept, r_value, p_value, std_err = vr.Fitter(lx2,ly2, np.min(lx2), np.max(lx2) )
#        slope_lst[i] = slope
#    return slope_lst
