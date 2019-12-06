def Havefactor(n):
    if n%10==0:
        return True
    else:
        return False
num=int(input())
bg=0
bgwf=0
if Havefactor(num):
    bg=num+10
    print(bg)
else:
    factor=num%10
    wf=num-factor
    bgwf=wf+10
    print(bgwf)
    