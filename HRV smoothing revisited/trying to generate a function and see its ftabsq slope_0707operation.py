# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 18:47:54 2018

@author: Harry
"""

import numpy as np
import matplotlib.pyplot as plt
import FTABSQ_viewer_for_smoothing_test_re as vr

x= np.arange(1,10001)
y = x**(-0.008)
ft = np.fft.fft(y)
pd = np.abs(ft)**2


#lx = np.log(np.arange(1,len(pd)+1))
#ly = np.log(pd)
#plt.plot(lx, ly)
#plt.show()
#
#lx = np.log(np.arange(1,len(pd)+1))[:5001]
#ly = np.log(pd)[:5001]
#plt.plot(lx, ly)
#plt.show()

#lx = np.log(np.arange(1,len(pd)+1))[1:5001]
#ly = np.log(pd)[1:5001]
'''
#Alst =[11 , 8 , 7 , 6] #A list ori, archived
#Alst2 = [8 , 11 , 7 , 6]
#Alst3 = [7, 8, 11, 6]
#Alst4 = [8 , 7 , 6, 11]
#y1 = A1* x[0:2500]**(-0.00758) + A2* x[2500:5000]**(+0.00128) + A3* x[5000:7500]**(+0.01010) + A4* x[7500:10000]**(-0.01635) #y ori archived
#y2 = A1* x[2500:5000]**(-0.00758) + A2* x[0:2500]**(+0.00128) + A3* x[5000:7500]**(+0.01010) + A4* x[7500:10000]**(-0.01635)
#y3 = A1* x[5000:7500]**(-0.00758) + A2* x[2500:5000]**(+0.00128) + A3* x[0:2500]**(+0.01010) + A4* x[7500:10000]**(-0.01635)
'''
'''
for III 
Alst =[1 , 1 , 1, 1]
y = A1* x[0:2500]**(-0.00758) + A2* x[2500:5000]**(+0.00128) + A4* x[5000:7500]**(-0.01635) + A3* x[7500:10000]**(+0.01010)  
'''
'''
x= np.arange(1,10001)
y = np.array([A1* x[0:2500]**(-0.00758) , A2* x[2500:5000]**(+0.00128) , A3* x[5000:7500]**(+0.01010), A4* x[7500:10000]**(-0.01635)])  
還沒完全修正完錯誤之前
'''
'''
#y = np.array([A1* x1[0:2500]**(-0.00758) , A2* x1[0:2500]**(+0.00128) , A3* x1[0:2500]**(+0.01010), A4* x1[0:2500]**(-0.01635)])
'''
'''
Alst =[1 , 1 , 1, 1]
alpha = [-0.00758, 0.00128, -0.01635, 0.01010]
A1, A2, A3, A4 = Alst/np.sum(Alst)
x = np.arange(1,10001)
x1 = np.arange(1,2501)/2500
y = []
for i in range(0, len(Alst)):
    y_elem = Alst[i]* x1 ** alpha[i]
    y_elem = y_elem - (np.average(y_elem)) + 60/72
    y = np.append(y, y_elem)
y = y.flatten()
print(len(y))
ft = np.fft.fft(y)
pd = np.abs(ft)**2

x2 = np.arange(1,len(pd)+1)[1:5001]
y2 = pd[1:5001]
x2 = x2/np.max(x2)
y2 = y2/np.max(y2)
目前正確的寫法，archived , 0628 20:36
'''
#Alst =[11 , 8 , 7 , 6]
#Alst =[1 , 1 , 1, 1]
Alst = [8, 7, 5, 6, 4]
#Alst =[1 , 1 , 1, 1, 1]
alpha1 = [-0.00758, 0.00128, -0.01635, 0.01010]
alpha2 = [-0.00758, 0.01010 , -0.01635 , 0.00128]
alpha3 = [-0.00758, 2.01010 , -0.01635 , 0.00128]
alpha4 = [0.00445, -0.00304, 0.01194, -0.02552, 0.01943]
#A1, A2, A3, A4 = Alst/np.sum(Alst)
Alst =  Alst/np.sum(Alst)
xwl, xwu = [-7, -4]

#alpha = -np.array(alpha1)
alpha = np.array(alpha4)
#version 1-------------------
#x = np.arange(1,10001)
#x1 = np.arange(1,2501)/2500
#y = []
#for i in range(0, len(Alst)):
#    y_elem = Alst[i]* x1 ** alpha[i]
#    y_elem = y_elem - (np.average(y_elem)) + 60/72
#    y = np.append(y, y_elem)
#y = y.flatten()
#----------------------------
##version 2-------------------
#x = np.arange(1,10001)
#x1 = np.arange(1,2501)/2500
#y = [0]
#for i in range(0, len(Alst)):
#    y_elem = Alst[i]* x1 ** alpha[i]
#    if alpha[i] > 0 :
#        y_elem = y_elem - (np.max(y_elem)) + y[-1]
#    elif alpha[i] < 0 :
#        y_elem = y_elem - (np.min(y_elem)) + y[-1]
#    y = np.append(y, y_elem)
#y = y[1:].flatten()
##----------------------------
#version 3 varied x length-------------------
#[plen, elelen] = [12500, 2500]
#x = np.arange(1,plen+1)
#y = []
##xlst = [3000, 1000, 2500, 3500]
##xlst = [2500, 2500, 2500, 2500]
#xlst = [elelen+ 2000 , elelen +1000,  elelen-1000,  elelen,  elelen-2000]
#for i in range(0, len(Alst)):
#    x1 = (np.arange(1, xlst[i]+1))/(xlst[i]+1)
#    y_elem = Alst[i]* x1 ** alpha[i]
#    y_elem = y_elem - (np.average(y_elem)) + 60/72
##    y_elem = y_elem - (np.median(y_elem)) + 60/72
#    for j in range(0, xlst[i]):
#        y = np.append(y, y_elem[j])
#        
#y_longer = []
#for i in range(0, int(plen/elelen/2)):
#    y_longer = np.append(y_longer, y)
#y = y_longer
#----------------------------
#version 4 varied x length-------------------
#x = np.arange(1,10001)
#y = [60/72]
#xlst = [3000, 1000, 2500, 3500]
##xlst = [2500, 2500, 2500, 2500]
#for i in range(0, len(Alst)):
#    x1 = (np.arange(1, xlst[i]+1))/xlst[i]
#    y_elem = Alst[i]* x1 ** alpha[i]
#    if alpha[i] < 0 :
#        y_elem = y_elem - (np.max(y_elem))  + y[-1]
#    elif alpha[i] > 0 :
#        y_elem = y_elem - (np.min(y_elem))  + y[-1]
#    for j in range(0, xlst[i]):
#        y = np.append(y, y_elem[j])
#y = y[1:]
##----------------------------
#version 5 varied x length-------------------
[plen, elelen] = [12500, 2500]
x = np.arange(1,plen+1)
#xlst = [elelen+ 2000 , elelen +1000,  elelen-1000,  elelen,  elelen-2000]
xlst = [elelen,elelen,elelen,elelen,elelen]
y = [60/72]
#xlst = [3000, 1000, 2500, 3500]
#xlst = [2500, 2500, 2500, 2500]
for i in range(0, len(Alst)):
    x1 = (np.arange(1, xlst[i]+1))/xlst[i]
    y_elem = Alst[i]* x1 ** alpha[i]
    if alpha[i] < 0 :
        y_elem = y_elem - (np.min(y_elem))  + 60/72
    elif alpha[i] > 0 :
        y_elem = y_elem - (np.max(y_elem))  + 60/72
    for j in range(0, xlst[i]):
        y = np.append(y, y_elem[j])
y = y[1:]
#----------------------------
##version 6 varied x length-------------------
#[plen, elelen] = [12500, 2500]
#x = np.arange(1,plen+1)
##xlst = [elelen+ 2000 , elelen +1000,  elelen-1000,  elelen,  elelen-2000]
#xlst = [elelen,elelen,elelen,elelen,elelen]
#y = [60/72]
##xlst = [3000, 1000, 2500, 3500]
##xlst = [2500, 2500, 2500, 2500]
#for i in range(0, len(Alst)):
#    x1 = (np.arange(1, xlst[i]+1))/xlst[i]
#    #y_elem = Alst[i]* x1 ** alpha[i]
#    if alpha[i] < 0 :
#        y_elem = Alst[i]* x1 ** alpha[i]
#        y_elem = y_elem - (np.min(y_elem))  + 60/72
#    elif alpha[i] > 0 :
#        y_elem = (Alst[i]* (1-x1) ** alpha[i])
#        y_elem = y_elem - (np.max(y_elem))  + 60/72
#    for j in range(0, xlst[i]):
#        y = np.append(y, y_elem[j])
#y = y[1:]
##----------------------------

print(len(y))
ft = np.fft.fft(y)
pd = np.abs(ft)**2
hlf = int(np.round(len(pd)/2))

x2 = np.arange(1,len(pd)+1)[1:hlf]
y2 = pd[1:hlf]
x2 = x2/np.max(x2)
y2 = y2/np.max(y2)
#y2 = (y2+1)/(np.max(y2)+1)

#x3 = [x2[i] for i in range(0, len(y2)) if y2[i]> 0]
#y3 = [y2[i] for i in range(0, len(y2)) if y2[i]> 0]
#
#plt.plot(x3, y3)
#plt.title('PSD of Generated data with f(x) = Ai* xi ^alpha[i]')
#plt.ylabel('Log(PSD)')
#plt.xlabel('Log(sequence)')
#plt.show()
#lx = np.log(x3)
#ly = np.log(y3)
#slope, intercept, r_value, p_value, std_err = vr.Fitter(lx, ly, xwl, xwu)
#psu_y = lx*slope + intercept
#plt.plot(lx, ly)
#plt.plot(lx, psu_y,'r--')
#plt.title('LOGLOG PSD of Generated data with f(x) = Ai* xi ^alpha[i]')
#plt.annotate('Alpha ='+ str(alpha), xy = (0,0), xytext = (-6 ,-1), bbox=dict(boxstyle="round", fc="w"))
#plt.ylabel('Log(PSD)')
#plt.xlabel('Log(sequence)')
#plt.axvspan(xwl, xwu, color='grey', alpha=0.5)
#plt.show()





plt.plot(x, y)
#plt.plot(lx, psu_y,'r--')
plt.title('Generated data with f(x) = Ai* xi ^alpha[i]')
plt.annotate('Alpha ='+ str(alpha), xy = (8000 ,0.925), xytext = (8000 ,0.950), va='center', ha='center', bbox=dict(boxstyle="round", fc="w"))
plt.ylabel('T(artificial RR) (sec)')
plt.xlabel('sequence')
plt.show()


#-----------------------------------------------------------------------------
lx = np.log(x2)
ly = np.log(y2)
#lx = np.log(x3)
#ly = np.log(y3)
slope, intercept, r_value, p_value, std_err = vr.Fitter(lx, ly, xwl, xwu)
psu_y = lx*slope + intercept
plt.plot(lx, ly)
plt.plot(lx, psu_y,'r--')
plt.title('LOGLOG PSD of Generated data with f(x) = Ai* xi ^alpha[i]')
plt.annotate('Alpha ='+ str(alpha), xy = (0,0), xytext = (-6 ,-1), bbox=dict(boxstyle="round", fc="w"))
plt.ylabel('Log(PSD)')
plt.xlabel('Log(sequence)')
plt.axvspan(xwl, xwu, color='grey', alpha=0.5)
plt.show()

print('slope, intercept', slope, intercept)
print('A1 to A4 :', str(Alst))
print('X fitting range : ', [xwl, xwu])
#-----------------------------------------------------------------------------

#plt.plot(x, y)
##plt.plot(lx, psu_y,'r--')
#plt.title('Generated data with f(x) = A1* x[0:2500]**(-0.00758) + A2* x[2500:5000]**(+0.00128) + A4* x[5000:7500]**(-0.01635) + A3* x[7500:10000]**(+0.01010) ')
#plt.ylabel('T(artificial RR) (sec)')
#plt.xlabel('sequence')
#plt.show()