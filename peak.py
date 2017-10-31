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
