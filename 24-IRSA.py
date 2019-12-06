lts=[]
stl=[]
n=int(input())
for i in range(0,n):
    x1,x2= map(int, input().split())
    lts.append(x1)
    stl.append(x2)
# print(lts)
# print(stl)

# print("max value is :",max(lts))
# print("max value is :",max(stl))
# print("Find:",lts.index(max(lts)))
# print("Find:",stl.index(max(stl)))
max_price=lts.index(max(lts))
max_keifeat=stl.index(max(stl))
if max_price==max_keifeat:
    print("poor irsa")
else:
    print("happy irsa")