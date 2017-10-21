import math

def func(val):
	return math.tan(val) - 2*val

def solve(a, b, acc):
    if abs(func(a)) < acc:
    	return a
    elif abs(func(b)) < acc:
    	return b
    elif func(a)*func((a+b)/2) <=0:
    	return solve(a, (a+b)/2, acc)
    else:
    	return solve((a+b)/2, b, acc)
