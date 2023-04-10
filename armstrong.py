


n=int(input())
temp=n
f=n
num=0
c=0


h=(len(str(n)))

while temp>0:
    y=temp%10
    num=num+y**h
    temp//=10

if f==num:
    print('true')
else:
    print('false')