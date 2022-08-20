# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 15:02:33 2018

@author: Harry
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
freq_upper = 0.004
freq_lower = 0.0001
flst = ['ltdb_14046_RR_Sth1000_400_700.txt,Pseudo_ltdb_14046_RR_Sth1000_400_700.txt']
def Info_Print(filename, data, lower, upper):
    '''
    Print basic session information.
    '''
    lng = len(data)
    print('\n')
    print('Length of data : ', lng)
    tm = np.floor(lng * data[1]/ 3600)
    print('Estimated Time spent for this RR-measurement : ', tm ,' hrs')
    print('The lower and upper limit for the fitting \nare set as : ', str([lower, upper]), ' (Hz)')
    return 0
def Data_Process(rr):
    '''
    take raw data as seq of RR
    output [RR, RR-variability],[FTABSQ-RR, FTABSQ-RRV],[x value of first 1/10 of data FTASQRR, x value of first 1/10 of data FTASQRRV]
    '''
    rrv = np.array(rr - np.average(rr))
    FTASRR = np.power(np.abs(np.fft.fft(rr)),2)
    FTASRRV = np.power(np.abs(np.fft.fft(rrv)),2)
    rrhlf = np.floor_divide(len(FTASRR),2)
    rrvhlf = rrhlf = np.floor_divide(len(FTASRRV),2)
    rrxwu = rrhlf/10
    rrvxwu = rrvhlf/10
    return [ [rr,rrv], [FTASRR, FTASRRV], [rrhlf, rrvhlf], [rrxwu, rrvxwu] ]
def Drawer(xd, yd, xwl, xwu, settext):
    '''
    take data xd, yd
    take xwl xwu as value for axvspan
    take title as title, xlabel, ylabel as labels respectively.
    Non-log plot exlude the 1st point by default.
    log plot現在也去掉第0個點，而且是log 10為底
    '''
    [[title, xlabel, ylabel], [title2, xlabel2, ylabel2]] =  settext
    #===========================================
    #fig, ax = plt.subplots(1,1)
    #ax.plot(xd[1:], yd[1:])
    #ax.axvspan(xwl, xwu, color='grey', alpha=0.5)
    #ax.set_title(title)
    #ax.set_xlabel(xlabel)
    #ax.set_ylabel(ylabel)
    #plt.show()
    #===============loglog below=================
    #lxd = np.log(xd)
    #lyd = np.log(yd)
    lxd = np.log10(xd)[1:]
    lyd = np.log10(yd)[1:]
    lxwl, lxwu = np.log10(freq_lower), np.log10(freq_upper) 
    fit = Fitter(lxd, lyd, lxwl, lxwu)
        #reassign lwxl to make the graph more beautiful in the case of the Num of data are too few,
        #that lxwl is actually smaller than the lowest in lxd
        #beware that it is advised to fit first, then draw, so that the upper and lower bound don't get confused, bounds are strict for fitting,
        #and then can be loosen when drawing plots.
    if lxwl < np.min(lxd):
        lxwl = np.min(lxd)
    else:
        lxwl = lxwl
    lfit_yd = lxd*fit[0] + fit[1]
    fig1, ax1 = plt.subplots(1,1)
    ax1.plot(lxd, lyd,'.')
    ax1.plot(lxd, lfit_yd,'-r')
    ax1.axvspan(lxwl, lxwu, color='grey', alpha=0.5)
    ax1.set_title(title2)
    ax1.set_xlabel(xlabel2)
    ax1.set_ylabel(ylabel2)
    ax1.annotate('y = '+ str(np.round(fit[0],2)) +' x ' + str(np.round(fit[1],2)), xy=(0.1, 0.35), xycoords=ax1.transAxes)
    plt.show()
    return fit
def Freq_arr_gen(hlf, xwl, xwu):
    '''
    generate the frequency list, with max frequency set as 1 hz
    take xwl xwu as seq indicator and out put corresponding x value for boundary.
    '''
    fx = np.arange(1, hlf+1) 
    xwl = np.divide(xwl, np.max(fx))
    xwu = np.divide(xwu, np.max(fx))
    xd = np.divide(fx, np.max(fx))
    return [xd, xwl, xwu]
def Fitter(xd, yd, xwl, xwu):
    '''
    take data xd, yd
    take xwl xwu as value for fitting
    return slope, intercept, r_value, p_value, std_err
    '''
    bounded_xd, bounded_yd = np.transpose(np.array([ [xd[i], yd[i]] for i in range(0, len(xd)) if xwl< xd[i] < xwu]))
    slope, intercept, r_value, p_value, std_err = st.linregress( bounded_xd, bounded_yd )
    return slope, intercept, r_value, p_value, std_err
def Runbot(lst,  settext, ind_xwl):
    '''
    here rr in the pyfunction is just data, can be rr or rrv depending on the input lst
    '''
    [rr, FTASRR, rrhlf, rrxwu ] = lst
    fx, rrxwl, rrxwu = Freq_arr_gen(rrhlf, ind_xwl, rrxwu)
    yd = np.divide(FTASRR[:rrhlf], np.max(FTASRR[:rrhlf]))
    #fit = fitter(fx, yd, rrxwl, rrxwu)
    fit = Drawer(fx, yd, rrxwl, rrxwu, settext)  
    #這裡還有bug，用fitter和drawer fit出的斜率不同(暫時略過，應該是drawer版本較正確)
    return fit