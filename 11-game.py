import random
for i in range(1,1000):
    Res=random.randint(1,99)
    print('Response is:',Res)
    ans=int(input('Enter your ans:'))
    name=input('Enter your name:')
    
    while Res!=ans:
        if Res>ans:
            print('Response is big')
            ans=int(input('entr your ans:'))
        else:
            print('Respose is small')
            ans=int(input('entr your ans:'))
    print('congracholation',name)
    con=input('Would like continur[y,n]?')
    if con!='y':
        print('TNX',name)
        break
# con=input('Would like continur[y,n]?')

