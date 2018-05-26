#generate a random list whose length is N, mean is a given number from a given list
from random import randint, shuffle

li = [i for i in range(1, 20, 2)]

N = 100

randli = []

def mean_rand(mean, li, N):
    #mean:the mean of the random list
    #li:given list
    #N:random list length

    while True:
        randlist = []

        for i in range(N-1):
            num = randint(0, len(li)-1)
            randlist.append(li[num])
    
        last = mean*N - sum(randlist)
    
        randlist.append(last)
    
        if last in li:
            return randlist

for i in range(int(N/10)):
    
    temp_li = mean_rand(7, li, 10)
    
    for elem in temp_li:
        randli.append(elem)

shuffle(randli)

print(randli)
