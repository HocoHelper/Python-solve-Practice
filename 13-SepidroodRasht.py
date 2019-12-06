
lst = [] 

for i in range(0, 30): 
	ele = int(input()) 

	lst.append(ele) 
	 
count_0=lst.count(0)
count_1=lst.count(1)
count_3=lst.count(3)
total=count_3*3+count_1
print(total, count_3)



