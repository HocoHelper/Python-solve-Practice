lst=[]
def check(name_lst):
    newstring ='' 
    for a in name_lst: 
	    if (a.isupper()) == True: 
		    newstring+=(a.lower()) 
	    elif (a.islower()) == True: 
		    newstring+=(a.lower())
    print(newstring.capitalize())

for i in range(0,10):
    string=input()
    lst.append(string)
    # check(lst[i])
    # newstring=check(lst[i]).capitalize()
# print(lst)
for ii in range(len(lst)):
    check(lst[ii])



