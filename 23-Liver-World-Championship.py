n = int(input()) 

a = list(map(int,input().strip().split()))[:n] 

res = all(ele <=2 for ele in a) 
if res==True:
    m=n/3
    print(int(m))
count = sum(map(lambda x : x<=2, a))
m=count/3
print(int(m))
