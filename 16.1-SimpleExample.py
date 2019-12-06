string='sallam man Hoco Helper hastem'
print(len(string))
# for harf in range(0,len(string)):
#     print('Number Harf',harf,string[harf])

# this one is better then in python 
for harf in string:
    print(harf)
# this one is for count a
count=0
for harf in string:
    if harf=='a':
        count+=1
print('--------')
print('count of A :',count)

print('--------')
print(string[:6])
print('--------')
print(string[7:])
print('--------')
print(string[11:23])
print('--------')
print('H'+string[-5:])
print('--------')
string2=string[:-6]+'H'+string[-5:]
print(string2)
print('--------')