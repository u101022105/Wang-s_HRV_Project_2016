# -*- coding: utf-8 -*-
"""
Created on Mon May 21 21:00:49 2018

@author: Harry
This py is intended to draw nice graphs for fft, ATM, would like to implement 
just FTABSQ method of variability and period. Using PSD, normalized to max at 1.
With line regress fitting function. Show range for fitting, fitted slope. 
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
freq_upper = 0.004
freq_lower = 0.0001
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
#///////////////////////////////////////////////////////////////////
'''
here I listed some filenames
RR_ltdb-14046.txt
RR_ltdb-14134.txt
RR_ltdb-14149.txt
RR_ltdb-14157.txt
RR_ltdb-14172.txt
RR_ltdb-14184.txt
RR_svdb-800.txt
RR_svdb-801.txt
'''
#//////////////////////////////////////////////////////////////////////////op below
#filename = 'RR_U_hbT_ltdb-14046.txt'
#fessence = 'ltdb-14046'
#filename = 'RR_ltdb-14157.txt'
#flst = ['RR_ltdb-14046.txt',
#'RR_ltdb-14134.txt',
#'RR_ltdb-14149.txt',
#'RR_ltdb-14157.txt',
#'RR_ltdb-14172.txt',
#'RR_ltdb-14184.txt']
#flst = ['ltdb_14046_RR_Sth1000_400_700.txt,Pseudo_ltdb_14046_RR_Sth1000_400_700_10000.txt]
#flst= ['Pseudo_ltdb_14046_RR_Sth1000_400_700_10000.txt']
#flst=['RR_ltdb-14046.txt']
#flst = ['RR_ltdb-14046.txt','ltdb_14046_RR_400_700_expandedto5980.txt','Pseudo_ltdb_14046_RR_Sth1000_400_700_1000_alt.txt']
#flst = ['RR_ltdb-14046.txt','Pseudo_ltdb14046_RR_Sth1000_400_700_1000_alt.txt']
flst = ['RR_ltdb-14046.txt','Arch_Pseudo_ltdb14046_RR_Sth1000_400_700_1000_Gen4_inrrdataformat.txt']

#for i in range(0, len(flst)):
#    filename = flst[i]
#    fessence = filename[3:-4]
#    data = np.genfromtxt(filename, usecols = 0)[1:] 
#    Drawer(data[], data)

for i in range(0, len(flst)):
    filename = flst[i]
    fessence = filename[3:-4]
    data = np.genfromtxt(filename, usecols = 0)[1:]                                 #因為通常RR量測第一個點並不是真的RR間距，而是第0秒到第一個Rpeak的時間，所以去掉第0個點
    lst = Data_Process(data)
    [ [rr,rrv], [FTASRR, FTASRRV], [rrhlf, rrvhlf], [rrxwu, rrvxwu] ] = lst
    rrlst = np.array(lst).T[0]
    rrvlst = np.array(lst).T[1]
    rrtxt = [['Power Spectral Density of RR-interval from '+ str(fessence)+'\n','Frequency(Hz)','Relative Power'],['Double-Log-Plot of PSD RR-interval from '+ str(fessence),'Log(Frequency)','Log(Relative Power)']]
    rrvtxt = [['Power Spectral Density of RR-Variability from'+ str(fessence)+'\n','Frequency(Hz)','Relative Power'],['Double-Log-Plot of PSD RR-Variability from '+ str(fessence),'Log(Frequency)','Log(Relative Power)']]
    
    #plt.plot(np.log(np.arange(1,5001)/5000),np.log(FTASRR[0:5000]/np.max(FTASRR[0:5000])))
    #plt.show()
    #////////////////RUNNING through the pipeline//////////////////////////////
    Info_Print(fessence, data, freq_lower, freq_upper)
    fitrr = Runbot(rrlst, rrtxt, 2)
    print('RR resulted slope : ', fitrr[0])
    print('R^2 value ', fitrr[2]**2)
#    fitrrv = Runbot(rrvlst, rrvtxt, 2)
#    print('RRV resulted slope : ', fitrrv[0])
#    print('R^2 value ', fitrrv[2]**2)    
    

filename = 'ltdb_14046_RR_400_700_expandedto119600.txt'
fessence = filename[3:-4]
data = np.genfromtxt(filename, usecols = 0)[1:]                                 #因為通常RR量測第一個點並不是真的RR間距，而是第0秒到第一個Rpeak的時間，所以去掉第0個點
lst = Data_Process(data)
[ [rr,rrv], [FTASRR, FTASRRV], [rrhlf, rrvhlf], [rrxwu, rrvxwu] ] = lst
rrlst = np.array(lst).T[0]
rrvlst = np.array(lst).T[1]
rrtxt = [['Power Spectral Density of RR-interval from '+ str(fessence)+'\n','Frequency(Hz)','Relative Power'],['Double-Log-Plot of PSD RR-interval from '+ str(fessence),'Log(Frequency)','Log(Relative Power)']]
rrvtxt = [['Power Spectral Density of RR-Variability from'+ str(fessence)+'\n','Frequency(Hz)','Relative Power'],['Double-Log-Plot of PSD RR-Variability from '+ str(fessence),'Log(Frequency)','Log(Relative Power)']]

#plt.plot(np.log(np.arange(1,5001)/5000),np.log(FTASRR[0:5000]/np.max(FTASRR[0:5000])))
#plt.show()
#////////////////RUNNING through the pipeline//////////////////////////////
Info_Print(fessence, data, freq_lower, freq_upper)
fitrr = Runbot(rrlst, rrtxt, 2)
print('RR resulted slope : ', fitrr[0])
print('R^2 value ', fitrr[2]**2)