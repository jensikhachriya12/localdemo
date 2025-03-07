def convert_second(time):
    hour, minute,second = map(int,time.split(':'))
    seconds=(hour*3600)+(minute*60)+second
    return seconds

time=input("enter time:")
result=convert_second(time)
print("result:",result)

