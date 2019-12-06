import bisect
import math
lst=[]
llt=[]
def find_all_factors(n):
    factors = []
    for i in range(1, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            bisect.insort(factors,i)
            cofactor = n // i
            if i != cofactor: bisect.insort(factors, cofactor)
    return factors

for i in range(0,20):
    nume=int(input())
    lst.append(nume)
    facotors=find_all_factors(lst[i])
    len_facotors=len(find_all_factors(lst[i]))
    llt.append(len_facotors)
    max_factors=max(llt)


index=llt.index(max_factors)
number=lst[index]
print(number,max_factors)



    
 

