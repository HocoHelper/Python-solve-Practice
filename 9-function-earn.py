def IsCorrect(n):
    if n>=8:
        return False
    else:
        return True
def hoghoogh(hour,pay_hour):
        pay=hour*pay_hour
        return pay


hour_client=int(input('How many Time?'))
pay_hour_client=2
if IsCorrect(hour_client):
    print('We will pay ',hoghoogh(hour_client,pay_hour_client),'$')
else:
    print('It not correct')