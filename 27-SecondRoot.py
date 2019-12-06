import math 
import random  
import decimal
lts=[]

def truncate(f):
    return math.floor(f * 10 ** 4) / 10 ** 4
n = int(input())

def squareRoot(n):
    x=n
    y=1.000000 #iteration initialzation.
    e=0.000001 #accuracy after decimal place.
    while x-y > e:
        x=(x+y)/2
        y=n/x
    return x

for i in range(n):
    usrinp = int(input())
    nthRootValue = squareRoot(usrinp)
    lts.append(nthRootValue)

for number in lts:
    print("{0:.4f}".format(truncate(number)))

    

