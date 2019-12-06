from collections import OrderedDict 
n = int(input())
d = OrderedDict()

for i in range(n):
    keys,values = input().split() 
    d[keys] = values

sen=input()

for word, initial in d.items():
    sen = sen.replace(word.lower(), initial)

print (sen)