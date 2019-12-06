string=input() 
count1 = 0
count2 = 0

for a in string: 
# Checking for lowercase letter and converting to uppercase. 
	if (a.isupper()) == True: 
		count1+= 1 
# Checking for uppercase letter and converting to lowercase. 
	elif (a.islower()) == True: 
		count2+= 1
if count1>count2:
    print(string.upper())
else:
    print(string.lower())

