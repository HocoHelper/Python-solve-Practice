import math
x1,x2,x3= map(int, input().split())
# print(x1,x2,x3)
ave=(x1+x2+x3)/3
x1_dis=x1-ave
x2_dis=x2-ave
x3_dis=x3-ave
distace=abs(x1_dis)+abs(x2_dis)+abs(x3_dis)
# print(ave)
# print(x1_dis,x2_dis,x3_dis)
print(int(distace))