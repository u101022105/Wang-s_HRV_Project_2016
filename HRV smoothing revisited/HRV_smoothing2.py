# -*- coding: utf-8 -*-
"""
Created on Wed May 16 17:22:35 2018

@author: Harry
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

def draw(data, title, mode, lbl):
    '''
    draw basic matplot, mode= 0 when data is y value,
    mode =1 when data contains both x and y. mode = 2 for loglog
    lbl = labels list [xlabel, ylabel, show_coor]
    '''
    if mode == 0:
        #y = data
        y = data[1]
        x = np.arange(0,len(data))
        fig0, ax0 = plt.subplots(1,1)
        ax0.set_title(title)
        ax0.plot(x,y,'.r')
        ax0.plot(x,y,'-')
        plt.show()
    
    elif mode == 5:
        y = data[1]
        x = data[0]
        if type(lbl) == list:
            xlbl, ylbl = lbl[0], lbl[1]
            fig0, ax0 = plt.subplots(1,1)
            ax0.set_title(title)
            ax0.set_xlabel(xlbl)
            ax0.set_ylabel(ylbl)
            ax0.grid(True)
            ax0.plot(x,y,'.r')
            ax0.plot(x,y,'-b')
        else:
            fig0, ax0 = plt.subplots(1,1)
            ax0.set_title(title)
            ax0.grid(True)
            ax0.plot(x,y,'.r')
            ax0.plot(x,y,'-b')
            
        fig0.set_size_inches(28, 14)
        if lbl[3] == 1:
            xt = np.arange(x[0], x[-1], step= 1000)
            yt = np.arange(round(y.min(), 3), round(y.max(), 3), step= 0.01)
            ax0.set_xticks(xt)
            ax0.set_xticklabels(xt,rotation ="vertical")
            ax0.set_yticks(yt)
            ax0.set_yticklabels(yt)
        #fig0.savefig('test2png.png', dpi=100)
        if lbl[2] == 1:
            for i,j in zip(x,y):
                ax0.annotate('({0:.0f} '.format(i) + ', {0:.4f})'.format(j),xy=(i,j))
        plt.show()
        
    elif mode == 1:
        y = data[1]
        x = data[0]
#        stp = data[2]
        stp = 2000
        fig0, ax0 = plt.subplots(1,1)
        ax0.set_title(title)
        ax0.plot(x,y,'.r')
        ax0.plot(x,y,'-')
        xt = np.arange(x[0], x[-1], step= stp)
        ax0.set_xticks(xt)
        ax0.set_xticklabels(xt,rotation ="vertical")
        plt.show()
    elif mode == 2:
        y = data[1]
        x = data[0]
        #stp = data[2]*100
        stp = 0.02
        fig0, ax0 = plt.subplots(1,1)
        ax0.set_title(title)
        ax0.plot(x,y,'.r')
        ax0.plot(x,y,'-')
#        xt = np.arange(x[0], x[-1], step= stp)
        xt = np.arange(4.65, 4.92, step= stp)
        ax0.set_xticks(xt)
        ax0.set_xticklabels(xt,rotation ="vertical")
        plt.show()
    elif mode == 3:
        y = data[1]
        x = data[0]
        stp = data[2]
        stp = 2000
        fig0, ax0 = plt.subplots(1,1)
        ax0.set_title(title)
        ax0.plot(x,y,'.r')
        ax0.plot(x,y,'-')
        plt.show()
    elif mode == 4:
        '''
        natural log mode
        '''
        y = data[1]
        x = data[0]
        #stp = data[2]*100
        stp = 0.02
        fig0, ax0 = plt.subplots(1,1)
        ax0.set_title(title)
        ax0.plot(x,y,'.r')
        ax0.plot(x,y,'-')
#        xt = np.arange(x[0], x[-1], step= stp)
        A = np.log10(np.e)
        xt = np.arange(4.65/A, 4.92/A, step= stp/A)
        ax0.set_xticks(xt)
        ax0.set_xticklabels(xt,rotation ="vertical")
        plt.plot
    return 0

def smooth1(data, n):
    lng = len(data)
    #sec_lng = int(sec_lng)
    inc = int(lng/n)
    x = np.array([])
    y = np.array([]) 
    i = 0
    print('\nsmoothing increment: ',inc , '\n points to be averaged into one value')
    while i*inc < lng:
        avg = np.average(data[i*inc: (i+1)*inc])
        x = np.append(x, (i)*inc)
        y = np.append(y, avg)
        i = i + 1
    result = np.vstack([x,y])
    #print(result)
    return result, inc

def smoothwxy(data, n):
    x_d = data[0]
    y_d = data[1]
    lng = len(data)
    #sec_lng = int(sec_lng)
    inc = int(lng/n)
    x = np.ndarray([])
    y = np.ndarray([]) 
    i = 0
    while i*inc < x_d[-1]:
        avg = np.average(y_d[i*inc: (i+1)*inc])
        x = np.append(x, (i+1)*inc)
        y = np.append(y, avg)
        i = i + 1
    result = np.vstack([x,y])
    #print(result)
    return result
def gen(seq, sec):
    '''
    seq = [[x10,y10], [x11, y11], [x20,y20], [x21, y21]....]
    sec = [xsec, ysec]
    sec = section amount 
    '''
    [xsec, ysec] = sec
    xlst=[]
    ylst=[]
    i = 0
    while i < len(seq):
        x = np.linspace(seq[i][0], seq[i+1][0], xsec)
        y = np.linspace(seq[i][1], seq[i+1][1], ysec)
        xlst = np.append(xlst, x)
        ylst = np.append(ylst, y)
        i= i+2
    res = np.vstack((xlst,ylst))
    return res
def gen2(seq, sec):
    '''
    This is assuming the model is logX-logY, so that res of gen2 gives back to X and Y by taking Exponential of 10.
    seq = [[x10,y10], [x11, y11], [x20,y20], [x21, y21]....]
    sec = [xsec, ysec]
    sec = section amount 
    '''
    [xsec, ysec] = sec
    xlst=[]
    ylst=[]
    i = 0
    while i < len(seq):
        x = np.power(10, np.linspace(seq[i][0], seq[i+1][0], xsec) )
        y = np.power(10, np.linspace(seq[i][1], seq[i+1][1], ysec) )
        xlst = np.append(xlst, x)
        ylst = np.append(ylst, y)
        i= i+2
    res = np.vstack((xlst,ylst))
    return res
def gen3(seq, sec):
    '''
    This is assuming the model is logX-logY, so that res of gen2 gives back to X and Y by taking Exponential of 10.
    seq = [[x10,y10], [x11, y11], [x20,y20], [x21, y21]....]
    sec = [xsec, ysec]
    sec = section amount 
    '''
    [xsec, ysec] = sec
    xlst=[]
    ylst=[]
    i = 0
    while i < len(seq): 
#        x = np.linspace(seq[i][0], seq[i+1][0], xsec)
        x = np.linspace(np.power(10,seq[i][0]), np.power(10,seq[i+1][0]), xsec) #此x屬於此編號i段
#        dx = (np.power(10,seq[i+1][0])-np.power(10,seq[i][0]))/xsec
        dx = 1
        #dx = (x[j+1]-x[j]) #此部和上一行相同dx = (np.power(10,seq[i+1][0])-np.power(10,seq[i][0]))/xsec，只是減少電腦重複計算 
        m = ((seq[i+1][1]-seq[i][1])/(seq[i+1][0]-seq[i][0]))
        #tempx = [np.power(10,seq[i][0]) + (dx*j) for j in range(1, xsec)]
        tempy = [ np.power(10,seq[i][1]) + np.power((dx*j),m ) if j> 0  else np.power(10,seq[i][1]) for j in range(0, xsec)]
#        tempy = [seq[i][1] + np.power((dx*j),m ) if j> 0  else seq[i][1] for j in range(0, xsec)]
        #tempx = np.insert(tempx, 0, seq[i][0])
        #tempy = np.power(x, m)
        #tempy = tempy-np.min(tempy)+seq[i][1]
        #tempy = np.insert(tempy, 0, np.power(10,seq[i][1]))
        xlst = np.append(xlst, x)
        ylst = np.append(ylst, tempy)
        i= i+2
            #fig, ax = plt.subplots(1,1)
            #ax.plot(xlst,ylst)
            #ax.set_ylim([-0.5, 2])
            #plt.show()
        #    xlst = np.power(10, xlst)
        #    ylst = np.power(10, ylst)
    ylst = np.log10(ylst)
    res = np.vstack((xlst,ylst))
    return res
def gen4(seq, sec):
    '''
    This is assuming the model is logX-logY, so that res of gen2 gives back to X and Y by taking Exponential of 10.
    seq = [[x10,y10], [x11, y11], [x20,y20], [x21, y21]....]
    sec = [xsec, ysec]
    sec = section amount 
    '''
    [xsec, ysec] = sec
    xlst=[]
    ylst=[]
    i = 0
    while i < len(seq): 
#        x = np.linspace(seq[i][0], seq[i+1][0], xsec)
#        lx = np.linspace(seq[i][0], seq[i+1][0], xsec) #此x屬於此編號i段
#        x = np.exp(lx)
        x = np.linspace(np.exp(seq[i][0]), np.exp(seq[i+1][0]), xsec)
#        dx = (np.power(10,seq[i+1][0])-np.power(10,seq[i][0]))/xsec
        #dx = (x[j+1]-x[j])
        #dx = (x[j+1]-x[j]) #此部和上一行相同dx = (np.power(10,seq[i+1][0])-np.power(10,seq[i][0]))/xsec，只是減少電腦重複計算 
        m = ((seq[i+1][1]-seq[i][1])/(seq[i+1][0]-seq[i][0]))
        #tempx = [np.power(10,seq[i][0]) + (dx*j) for j in range(1, xsec)]
        #temply = [ seq[i][1] + np.power(((x[j+1]-x[j])),m ) if j> 0  else np.power(10,seq[i][1]) for j in range(0, xsec)]
        #tempy = [seq[i][1] + np.power((dx*j),m ) if j> 0  else seq[i][1] for j in range(0, xsec)]
        #tempx = np.insert(tempx, 0, seq[i][0])
        #tempy = np.power(x, m)
        #tempy = tempy-np.min(tempy)+seq[i][1]
        #tempy = np.insert(tempy, 0, np.power(10,seq[i][1]))
            #temply = [ seq[i][1] + (lx[j+1]-lx[j])*m  if j> 0  else seq[i][1] for j in range(0, xsec-1)]
            #xlst = np.append(xlst, x[:-1])
        #temply = [ seq[i][1] + (j/xsec)*m  if j> 0  else seq[i][1] for j in range(0, xsec)]
        temply = [ seq[i][1] + (j/xsec)*m  if j> 0  else seq[i][1] for j in range(0, xsec)]
        xlst = np.append(xlst, x)
        ylst = np.append(ylst, np.exp(temply))
        #ylst = ylst/np.max(ylst)
        i= i+2
    ylst = ylst/np.max(ylst)
    res = np.vstack((xlst,ylst))
    #print(np.shape(res))
    return res
    
def PSD(datay):
    ft= np.fft.fft(datay)
    hlf = int(len(ft)/2)
    ps = np.power(np.abs(ft),2)
    psd = ps/ np.max(ps)
    lpsd = np.log10(psd[0:hlf])
    x = np.arange(1, hlf+1)
    x = x/ np.max(x)
    lx = np.log10(x)
    fig, ax = plt.subplots(1,1)
#    d = np.vstack((lx,lpsd)).T
    ax.plot(lx ,lpsd,'-')
    ax.plot(lx, lpsd,'.r')
    plt.show()
#def smoothwxy(data, sec_lng):
#    x_d = data[0]
#    y_d = data[1]
#    sec_lng = int(sec_lng)
#    x = np.ndarray([])
#    y = np.ndarray([]) 
#    i = 0
#    while i* sec_lng < x_d[-1]:
#        avg = np.average(y_d[i*sec_lng: (i+1)*sec_lng])
#        x = np.append(x, i* sec_lng)
#        y = np.append(y, avg)
#        i = i + 1
#    result = np.vstack([x,y])
#    #print(result)
#    return result

#filename = 'RR_U_hbT_ltdb-14046.txt'
#filelist = ['RR_ltdb-14046.txt',
#'RR_ltdb-14134.txt',
#'RR_ltdb-14149.txt',
#'RR_ltdb-14157.txt',
#'RR_ltdb-14172.txt',
#'RR_ltdb-14184.txt']
#filename = filelist[0]
#data = np.genfromtxt(filename, usecols = 0)
#lng = len(data)
##print('The full raw length of this data set is :', lng)
#print('length of data = ', lng)
#n = 1000
#sec_lng = lng/n #把原資料分成n份，每份所需長度為sec_lng
#bn = int(np.floor_divide(lng, sec_lng))
##psu_smooth = np.histogram(data, bins = bn) #hist[0] = amount = y; hist[1] = position = x
#sm1, inc1 = smooth1(data, n)
#[ini,end] = [400,700]
#nsm1x = sm1[0][400:700]
#nsm1y = sm1[1][400:700]/np.max(sm1[1][400:700]) #normalize height
##___________________________Drawing raw and smoothed data___________________________
##draw(data, 'Raw RR-t, file = '+ filename, 0)
##draw([sm1[0], sm1[1],inc1], '1st attempt of smoothing RR-t, file = '+ filename + ' cut into {:d} sections'.format(n), 1)
#draw([sm1[0][ini:end], sm1[1][ini:end], inc1], '1st attempt of smoothing RR-t, showing first '+str(end)+' segments, file = '+ filename + ' cut into {:d} sections'.format(n), 1)
###print('sm1 x, y [0:10]',[sm1[0][0:10], sm1[1][0:10]])
##sm1lx = [np.log(sm1[0][i]) for i in range(ini, end)]
##sm1ly = [np.log(sm1[1][i]) for i in range(ini, end)]
##tempname = 'loglog smoothing RR-t, showing first '+str(end)+' segments, file = '+ filename + ' cut into {:d} sections'.format(n)
##draw([sm1lx, sm1ly, np.log(inc1)], tempname, 4)
#
#tempname = 'Normalized smoothing RR-t, from '+str(end)+' segments, file = '+ filename + ' cut into {:d} sections'.format(n)
#draw([nsm1x, nsm1y, np.log(inc1)], tempname, 5)
#
#sm1lx = [np.log(nsm1x) for i in range(ini, end)]
#sm1ly = [np.log(nsm1y) for i in range(ini, end)]
#tempname = 'loglog normalized smoothing RR-t, from '+str(end)+' segments, file = '+ filename + ' cut into {:d} sections'.format(n)
#draw([sm1lx, sm1ly, np.log(inc1)], tempname, 5)
##---------------------------Drawing raw and smoothed data---------------------------
#
##___________________________Generating x y from model of smoothed data___________________________
#seq = [[4.660,-0.158],[4.685,	-0.095],[4.685,	-0.120],[4.730,	-0.140],[4.731,	-0.140],[4.790,	-0.070],[4.791,	-0.135],[4.830,	-0.160],[4.831,	-0.160],[4.885,	-0.110],[4.890,	-0.140],[4.910,	-0.105]]
##psu_data = gen(seq, [10,10])
##psu_data2 = gen2(seq, [1000,1000])
#psu_data2_2 = gen3(seq, [1000,1000])
#draw(psu_data, 'Pseudo data of smoothed loglog ltdb14046[400:700] T-t', 2)
#draw([psu_data2[0], psu_data2[1], 30], 'Pseudo data of smoothed ltdb14046[400:700] T-t', 3)
#psu_data2_2x = np.genfromtxt('Pseudo_ltdb_14046_RR_Sth1000_400_700_1000_alt.txt', usecols = 0)
#psu_data2_2y = np.genfromtxt('Pseudo_ltdb_14046_RR_Sth1000_400_700_1000_alt.txt', usecols = 1)

#draw([psu_data2_2[0], psu_data2_2[1], 30], 'Pseudo data of smoothed ltdb14046[400:700] T-t', 3)

#with open('Pseudo_ltdb14046_RR_Sth1000_400_700_1000_alt.txt', 'w') as f:
#    x = psu_data2_2[0]
#    y = psu_data2_2[1]
#    res = np.transpose(np.vstack([x,y]))
#    temp = [f.write(str(res[i])[3:-2]+'\n') for i in range(0, len(res))]
#---------------------------Generating x y from model of smoothed data---------------------------

#___________________________FFT abs sqr___________________________

#    
#psu_data3 = np.genfromtxt('Pseudo_ltdb_14046_RR_Sth1000_400_700_1000.txt', usecols = 1) 
#psu_data4 = np.genfromtxt('ltdb_14046_RR_400_700_expandedto2990.txt', usecols = 1)
##psu_data3 = psu_data2[1]   
#PSD(psu_data3)
#PSD(psu_data4)

#PSD(psu_data2_2[1])



#---------------------------FFT abs sqr---------------------------



#___________________________Output smoothed data___________________________
#with open('ltdb14046_RR_Sth1000_400_700.txt', 'w') as f:
#    [ini,end] = [400,700]
#    x = sm1[0][ini:end]
#    y = sm1[1][ini:end]
#    res = np.transpose(np.vstack([x,y]))
#    temp = [f.write(str(res[i])[1:-2]+'\n') for i in range(0, len(res))]
#---------------------------Output smoothed data---------------------------
#x1 = np.genfromtxt('ltdb14046_RR_Sth1000_400_700.txt', usecols = 0)
#y1 = np.genfromtxt('ltdb14046_RR_Sth1000_400_700.txt', usecols = 1)
#draw([x1,y1], 'test on retrieve',1)
#    i = 0
#    while i < 300:
##        f.write(str(x[i])+'\t'+str(y[i]))
#        f.write(str(x[i]))
#        i=+1

#===============================================================================
#===============================================================================
#fig0, ax0 = plt.subplots(1,1)
#ax0.set_title('Raw RR-t, file = '+ filename)
#x,y = np.arange(0,lng), data  #the right most edge is excluded since it was just given but was abundant here.
#ax0.plot(x,y)
#plt.plot
#
#fig2, ax2 = plt.subplots(1,1)
#ax2.set_title('1st attempt of smoothing RR-t, file = '+ filename + ' cut into {:d} sections'.format(n))
#x,y = sm1[0], sm1[1]  #the right most edge is excluded since it was just given but was abundant here.
#ax2.plot(x,y, '-')
#plt.plot

#sm12 = smoothwxy(sm1, 10)
##sm12 = smoothwxy(sm12,10)
##sm12 = smooth1(sm12[1], 5)
#fig4, ax4 = plt.subplots(1,1)
#ax4.set_title('Double smoothing RR-t, file = '+ filename + ' cut into {:d} sections'.format(n))
#x,y = sm12[0], sm12[1] #the right most edge is excluded since it was just given but was abundant here.
#ax4.plot(x,y, '-*')
#plt.plot
#===============================================================================

#for i in range(0,10):
#    fig3, ax3 = plt.subplots(1,1)
#    m = 10 # increment of position
#    n = 0 + i* m # start position
#    ax3.set_title('Magnified at '+ str(n)+ ' for inc of '+ str(m) +' 1stAttemptofSmoothing RR-t, file = '+ filename + ' cut into {:d} sections'.format(n))
#    x,y = sm1[0][n:n+m], sm1[1][n:n+m]  #the right most edge is excluded since it was just given but was abundant here.
#    ax3.plot(x,y, '-*')
#    plt.plot

#fig3, ax3 = plt.subplots(1,1)
#m = 100 # increment of position
#n = 0  # start position
#ax3.set_title('Magnified at '+ str(n)+ ' for inc of '+ str(m) +' 1stAttemptofSmoothing RR-t, file = '+ filename + ' cut into {:d} sections'.format(n))
#x,y = sm1[0][n:n+m], sm1[1][n:n+m]  #the right most edge is excluded since it was just given but was abundant here.
#ax3.plot(x,y, '-*')
#plt.plot



#
#fig0, ax0 = plt.subplots(1,1)
#ax0.set_title('Raw RR-t, file = '+ filename)
#x,y = np.arange(0,lng), data  #the right most edge is excluded since it was just given but was abundant here.
#ax0.plot(x,y)
#plt.plot
#
#fig1, ax1 = plt.subplots(1,1)
#ax1.set_title('pseudo smoothing RR-t, file = '+ filename + ' cut into {:d} sections'.format(n))
#x,y = psu_smooth[1][:-1], psu_smooth[0]  #the right most edge is excluded since it was just given but was abundant here.
#ax1.plot(x,y)
#plt.plot

