#Cooley–Tukey FFT algorithm
import math, time
N = 1024

def W(N, r):
    return math.e**(-2*r*math.pi*1j/N)
    
def symme(a, N):
    s = str(bin(a))[2:]
    s = (int(math.log2(N)) - len(s))*"0" + s
    s = s[::-1]
    return int(''.join(s), 2)

def cal(li, m):
    y = [None for i in range(len(li))]

    for i in range(len(li)):
        if i%2**(m+1) == i%2**m:
            y[i] = li[i] + W(2**(m+1), i%(2**m))*li[i + 2**m]
        else:
            y[i] = li[i - 2**m] - W(2**(m+1), i%(2**m))*li[i]
    return y

def fft(li, N = None):
    if N == None:
        if int(math.log2(len(li))) == math.log2(len(li)):
            N = 2**(int(math.log2(len(li))))
        else:
            N = 2**(int(math.log2(len(li))) + 1)
    y = []
    if len(li) < N:
        temp = [0 for i in range(N - len(li))]
        li = li + temp
    for i in range(len(li)):
        y.append(li[symme(i, N)])
    for i in range(int(math.log2(N))):
        if i == 0:
            li = cal(y, i)
        else:
            li = cal(li, i)
    return li

start = time.time()
li = [i for i in range(1024)]
y = fft(li, 1024)
#numpy.fft.fft(li)
end = time.time() - start

