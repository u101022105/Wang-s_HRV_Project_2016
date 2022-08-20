# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 12:02:00 2018

@author: Harry
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

def PSD(data):
    '''
    take data, return  psdp, pdp
    psdp = (xsd, psd) which are x, y normalized and only kept the first half
    pdp = (x, pdp) which is unnormalized and only kept the first half
    '''
    lng = len(data)
    ft = np.fft.fft(data)
    pd = np.power(np.abs(ft),2)
    hlf = int(np.floor(lng/2))
    pd2 = pd[0:hlf]
    psd = pd2 / np.max(pd2)
    x = np.arange(1,hlf+1)
    x_f = np.arange(1, lng+1)
    xsd = x/ np.max(x)
    psdp = np.vstack((xsd, psd))
    pdp = np.vstack((x_f, pd))
    return psdp, pdp

def DRW(data, lbls):
    '''
    [ttle, xlbl, ylbl, size, ind] = lbls
    '''
    xd, yd = data
    [ttle, xlbl, ylbl, size, ind] = lbls
    fig0, ax0 = plt.subplots(1,1)
    ax0.set(title = ttle, xlabel = xlbl, ylabel = ylbl)
    fig0.set_size_inches(size[0],size[1])
    ax0.plot(xd, yd, '-')
    ax0.plot(xd, yd, 'r.')
    plt.show()
    return 0

def DRWLOG(data, lbls):
    '''
    [ttle, xlbl, ylbl, size, ind, rng] = lbls
    '''
    xd, yd = data
    [ttle, xlbl, ylbl, size, ind, rng] = lbls
    xwu, xwl = rng
    lxd = np.log(xd)
    lyd = np.log(yd)
    fig0, ax0 = plt.subplots(1,1)
    ax0.set(title = ttle, xlabel = xlbl, ylabel = ylbl)
    fig0.set_size_inches(size[0],size[1])
    ax0.axvspan(xwl, xwu, color='grey', alpha=0.5)
    ax0.plot(lxd, lyd, '-')
    ax0.plot(lxd, lyd, 'r.')
    bounded_xd, bounded_yd = np.transpose(np.array([ [lxd[i], lyd[i]] for i in range(0, len(lxd)) if xwl< lxd[i] < xwu]))
    fit = st.linregress(bounded_xd, bounded_yd)
    slope, intercept, r_value, p_value, std_err  = fit
    x_ann = np.arange(np.min(lxd), np.max(lxd))
    y_ann = x_ann * slope + intercept
    ax0.plot(x_ann, y_ann, 'k-')
    ax0.annotate('y = '+ str(np.round(fit[0],2)) +' x ' + str(np.round(fit[1],2)), xy=(0.1, 0.35), xycoords=ax0.transAxes)
    plt.show()
    return slope, intercept, r_value, p_value, std_err

def LOGFIT(data, lbls):
    '''
    [ttle, xlbl, ylbl, size, ind, rng] = lbls
    '''
    xd, yd = data
    [ttle, xlbl, ylbl, size, ind, rng] = lbls
    xwu, xwl = rng
    lxd = np.log(xd)
    lyd = np.log(yd)
#    fig0, ax0 = plt.subplots(1,1)
#    ax0.set(title = ttle, xlabel = xlbl, ylabel = ylbl)
#    fig0.set_size_inches(size[0],size[1])
#    ax0.axvspan(xwl, xwu, color='grey', alpha=0.5)
#    ax0.plot(lxd, lyd, '-')
#    ax0.plot(lxd, lyd, 'r.')
    bounded_xd, bounded_yd = np.transpose(np.array([ [lxd[i], lyd[i]] for i in range(0, len(lxd)) if xwl< lxd[i] < xwu]))
    fit = st.linregress(bounded_xd, bounded_yd)
    slope, intercept, r_value, p_value, std_err  = fit
#    x_ann = np.arange(np.min(lxd), np.max(lxd))
#    y_ann = x_ann * slope + intercept
#    ax0.plot(x_ann, y_ann, 'k-')
#    ax0.annotate('y = '+ str(np.round(fit[0],2)) +' x ' + str(np.round(fit[1],2)), xy=(0.1, 0.35), xycoords=ax0.transAxes)
#    plt.show()
    return slope, intercept, r_value, p_value, std_err