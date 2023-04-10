n=int(input())
temp=n
sum=0
for x in range(1,n):
    if n%x==0:

        sum=sum+x

if sum==temp:
    print('its perfect')
else:
    print('so sad vro its not perfect')
