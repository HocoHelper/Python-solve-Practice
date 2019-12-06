# Python program to find largest, smallest, 
# second largest and second smallest in a 
# list with complexity O(n)
lst=[]
def Range(list1): 
	largest = list1[0] 
	lowest = list1[0] 
	largest2 = None
	lowest2 = None
	for item in list1[1:]:	 
		if item > largest: 
			largest2 = largest 
			largest = item 
		elif largest2 == None or largest2 < item: 
			largest2 = item 
		if item < lowest: 
			lowest2 = lowest 
			lowest = item 
		elif lowest2 == None or lowest2 > item: 
			lowest2 = item 
			
	# print("Largest element is:", largest)  
	# print("Second Largest element is:", largest2) 
	print(largest,largest2)

while True:
    age=int(input())
    if age==-1:
        break
    lst.append(age)

Range(lst)
