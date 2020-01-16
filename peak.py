#给定范围求极值点及其区间
import math
def fun(x):
	return x*math.cos(x)

def fun(x):
	return 10*x + 70/x

def max_pole(arr, delta, num):
	x1 = arr[0]
	x2 = arr[1]
	for i in range(num):
		if fun((x1+x2-delta)/2) < fun((x1+x2+delta)/2):
			print(str((x1+x2-delta)/2) + " : "+str(fun((x1+x2-delta)/2)))
			print(str((x1+x2+delta)/2) + " : "+str(fun((x1+x2+delta)/2)))
			x1 = (x1+x2-delta)/2
		else:
			print(str((x1+x2-delta)/2) + " : "+str(fun((x1+x2-delta)/2)))
			print(str((x1+x2+delta)/2) + " : "+str(fun((x1+x2+delta)/2)))
			x2 = (x1+x2+delta)/2
		print([x1, x2])

def min_pole(arr, delta, num):
	x1 = arr[0]
	x2 = arr[1]
	for i in range(num):
		if fun((x1+x2-delta)/2) < fun((x1+x2+delta)/2):
			print(str((x1+x2-delta)/2) + " : "+str(fun((x1+x2-delta)/2)))
			print(str((x1+x2+delta)/2) + " : "+str(fun((x1+x2+delta)/2)))
			x2 = (x1+x2+delta)/2
		else:
			print(str((x1+x2-delta)/2) + " : "+str(fun((x1+x2-delta)/2)))
			print(str((x1+x2+delta)/2) + " : "+str(fun((x1+x2+delta)/2)))
			x1 = (x1+x2-delta)/2
		print([x1, x2])

from math import sin,isnan
from pylab import *
from scipy import signal

def peakdet(v, delta,thresh,x):
    delta=abs(delta)
    maxtab = []
    mintab = []

    v = asarray(v)

    mn, mx = v[0], v[0]
    mnpos, mxpos = NaN, NaN

    lookformax = True

    for i in arange(len(v)):
        this = v[i]
        if abs(this)>thresh:
            if this > mx:
                mx = this
                mxpos = x[i]
            if this < mn:
                mn = this
                mnpos = x[i]
            if lookformax:
                if (this < mx-delta):
                    if (mx>abs(thresh)) and not isnan(mxpos):
                        maxtab.append((mxpos, mx))
                    mn = this
                    mnpos = x[i]
                    lookformax = False
            else:
                if (this > mn+delta):
                    if (mn<-abs(thresh)) and not isnan(mnpos):
                        mintab.append((mnpos, mn))
                    mx = this
                    mxpos = x[i]
                    lookformax = True
    return array(maxtab), array(mintab)

#Input Signal
t=array(range(100))
series=0.3*sin(t)+0.7*cos(2*t)-0.5*sin(1.2*t)

thresh=0.95 #Threshold value
delta=0.0 #

a=zeros(len(t)) #
a[:]=thresh #

maxtab, mintab = peakdet(series,delta,thresh,t)

#Plotting output
scatter(array(maxtab)[:,0], array(maxtab)[:,1], color='red')
scatter(array(mintab)[:,0], array(mintab)[:,1], color='blue')
xlim([0,t[-1]])
title('Peak Detector')
grid(True)
plot(t,a,color='green',linestyle='--',dashes=(5,3))
plot(t,-a,color='green',linestyle='--',dashes=(5,3))
annotate('Threshold',xy=(t[-1],thresh),fontsize=9)
plot(t,series,'k')
show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import electrocardiogram
from scipy import signal

# input signal
x = np.arange(0,100,1)
y = 0.3 * np.sin(x) + 0.7 * np.cos(2 * x) - 0.5 * np.sin(1.2 * x)
threshold = 0

x = np.arange(2000)
y = electrocardiogram()[2000:4000]
# a = np.zeros(len(x))
# a[:] = threshold

 
b, a = signal.butter(8, (0.06, 0.14), 'bandpass')   #配置滤波器 8 表示滤波器的阶数
# >>> b, a = signal.butter(4, (0.003,0.009), 'bandpass', analog=True)
# >>> w, h = signal.freqs(b, a)
# >>> plt.semilogx(w, 20 * np.log10(abs(h)))
# >>> plt.title('Butterworth filter frequency response')
# >>> plt.xlabel('Frequency [radians / second]')
# >>> plt.ylabel('Amplitude [dB]')
# >>> plt.margins(0, 0.1)
# >>> plt.grid(which='both', axis='both')
# >>> plt.axvline(100, color='green') # cutoff frequency
# >>> plt.show()
filtedData = signal.filtfilt(b, a, y)  #data为要过滤的信号
plt.plot(x,filtedData)
plt.show()

maxi = np.where([(y - np.roll(y,1) >= 0) & (y - np.roll(y,-1) > 0)],y, np.nan)[0]
# max
# maxi = np.where(np.where([(y - np.roll(y,1) > 0) & (y - np.roll(y,-1) > 0)],y, 0)> threshold, y,np.nan)[0]
# min
# mini = np.where(np.where([(y - np.roll(y,1) < 0) & (y - np.roll(y,-1) < 0)],y, 0)< -threshold, y,np.nan)[0]

x_max = np.argwhere(~np.isnan(maxi))[:, 0]
# x_min = np.argwhere(~np.isnan(mini))[:, 0]

#Plotting output
plt.plot(x_max, maxi[x_max], 'x', color='green')
# plt.scatter(x_min, mini[x_min], color='blue')
plt.xlim([0,x[-1]])
plt.title('Peak Detector')
plt.grid(True)
# plt.plot(x,a,color='green',linestyle='--',dashes=(5,3))
# plt.plot(x,-a,color='green',linestyle='--',dashes=(5,3))
# plt.annotate('Threshold',xy=(x[-1],threshold),fontsize=9)
plt.plot(x,y,'k')
plt.show()


# >>> import matplotlib.pyplot as plt
# >>> from scipy.misc import electrocardiogram
# >>> from scipy.signal import find_peaks
# >>> x = electrocardiogram()[2000:4000]
# >>> peaks, _ = find_peaks(x, height=-10, threshold=-10)
# >>> plt.plot(x)
# >>> plt.plot(peaks, x[peaks], "x")
# >>> plt.plot(np.zeros_like(x), "--", color="gray")
# >>> plt.show()

from math import sin,isnan
from pylab import *
from scipy import signal

x = np.arange(1,100,1)
y = 0.3 * np.sin(t) + 0.7 * np.cos(2 * t) - 0.5 * np.sin(1.2 * t)
peakind = signal.find_peaks_cwt(y, np.arange(1,100))
