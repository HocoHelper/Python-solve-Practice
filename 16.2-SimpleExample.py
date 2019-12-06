a='sallam'
print(type(a))
print('-------------------------------------------------------------')
print(dir(a))
print('-------------------------------------------------------------')
help(a.count)
print('-------------------------------------------------------------')
b='bye' 
print(a>b)
print('-------------------------------------------------------------')
c='a'
d='A'
print('upercase & lowercase')
print(d>c)
print('-------------------------------------------------------------')
string='Sallam man Hoco Helper'
string2='   Sallm man Hoco Helper   '
# -------------------------------------------------------------------
print(string.upper())
print('-------------------------------------------------------------')
print(string.lower())
print('-------------------------------------------------------------')
print('first come (find)')
print(string.find('m'))
print('-------------------------------------------------------------')
print('second word start (find)')
print(string.find('m',6))
print('-------------------------------------------------------------')
print(string2)
print(string2.lstrip())
print('-------------------------------------------------------------')
print('len string')
print(len(string))
print('-------------------------------------------------------------')
print('conut of <<m>>')
print(string.count('m'))
print('-------------------------------------------------------------')
print('conut of <<m>> or <<M>>')
print(string.lower().count('m'))
print('-------------------------------------------------------------')
print('Is Start with <<h>>')
print(string.lower().startswith('h'))
print('-------------------------------------------------------------')
print('Is start with <<s>>')
print(string.lower().startswith('s'))
print('-------------------------------------------------------------')
print('This one is Simple')
name='MohmmadReza Norouzi'
age='21'
date_brif=1999
print('Hello',name,'How old are you?',age)
print('-------------------------------------------------------------')
print('This one is best')
print('my name is %s . How old are you ? %s <<%i>>' %(name,age,date_brif))