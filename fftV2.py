import math, time
from copy import deepcopy
N = 1024

def W(N, r):
    return math.e**(-2*r*math.pi*1j/N)
    
def symme(a, N):
    s = str(bin(a))[2:]
    s = (int(math.log2(N)) - len(s))*"0" + s
    s = s[::-1]
    return int(''.join(s), 2)

def cal(li, m):

    for i in range(len(li)):
        if i%2**(m+1) == i%2**m:
            y1 = li[i] + W(2**(m+1), i%(2**m))*li[i + 2**m]
            y2 = li[i] - W(2**(m+1), i%(2**m))*li[i + 2**m]
            li[i] = y1
            li[i+2**m] = y2
    return li

def cal01(li, N):
    y = [0]*N
    for i in range(len(li)):
        if i%2 == 0:
            y1 = li[symme(i, N)] + li[symme(i+1, N)]
            y2 = li[symme(i, N)] - li[symme(i+1, N)]
            y[i] = y1
            y[i+1] = y2
    return y


def fft(li, N = None):
    if N == None:
        if int(math.log2(len(li))) == math.log2(len(li)):
            N = 2**(int(math.log2(len(li))))
        else:
            N = 2**(int(math.log2(len(li))) + 1)
    y = deepcopy(li)
    if len(y) < N:
        temp = [0 for i in range(N - len(y))]
        y = y + temp
    
    for i in range(int(math.log2(N))):
        if i == 0:
            y = cal01(y, N)
        else:
            y = cal(y, i)
    return y

start = time.time()
li = [i for i in range(1024)]
y = fft(li, 1024)
#numpy.fft.fft(li)
end = time.time() - start
