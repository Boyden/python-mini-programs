import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import electrocardiogram
from scipy import signal


x = np.arange(2000)
y = electrocardiogram()[2000:4000]

plt.plot(y)
plt.title('ECG signal')
plt.xlabel('time points')
plt.ylabel('mV')
plt.show()

b, a = signal.butter(8, (0.06, 0.14), 'bandpass')
w, h = signal.freqs(b, a)
plt.semilogx(w, 20 * np.log10(abs(h)))
plt.title('Butterworth filter frequency response')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(100, color='green') # cutoff frequency
plt.show()

b, a = signal.butter(8, (0.06, 0.14), 'bandpass')   #配置滤波器 8 表示滤波器的阶数
filtedData = signal.filtfilt(b, a, y)  #data为要过滤的信号
plt.plot(x,filtedData)
plt.show()

maxi = np.where([(y - np.roll(y,1) >= 0) & (y - np.roll(y,-1) > 0)],y, np.nan)[0]
x_max = np.argwhere(~np.isnan(maxi))[:, 0]

#Plotting output
plt.plot(x_max, maxi[x_max], 'x', color='green')
plt.xlim([0,x[-1]])
plt.title('Peak Detector')
plt.grid(True)
plt.plot(x,y,'k')
plt.show()

rpeaks = ecg.christov_segmenter(y, sampling_rate=360).as_dict()['rpeaks']
plt.plot(rpeaks, y[rpeaks], 'x', color='green')
plt.xlim([0,x[-1]])
plt.title('Christov Peak Detector')
plt.grid(True)
plt.plot(x,y,'k')
plt.show()