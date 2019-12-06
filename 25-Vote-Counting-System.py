from collections import OrderedDict 
n=int(input())
lst=[]
d = OrderedDict()
for count in range(0,n):
    name=input()
    lst.append(name)

# print(lst)
# print(dict(Counter(lst)))
for word in lst:
    if word in d:
        d[word]=d[word]+1
    else:
        d[word]=1

for key in sorted(list(d.keys())) :
    print(key,d[key])