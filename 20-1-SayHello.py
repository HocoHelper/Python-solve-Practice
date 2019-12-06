from collections import OrderedDict
foo = input()
# check for how many l
count = 0
for i in foo: 
    if i == 'l': 
        count = count + 1

if count<=1:
    print('NO')
# delete duplicate
result = "".join(OrderedDict.fromkeys(foo))
# print(result)
if 'h' in result and 'e' in result and 'l' in result and 'o' in  result:
    print('YES')
# all(if 'h' in result:
#     )
# if "h" in result:
#     return True
# if "e" in result:
#     return True
# if "l" in result:
#     return True
# if 

