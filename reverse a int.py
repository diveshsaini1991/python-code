n=int(input())
r=0
while n>0:
    x=n%10
    r=r*10+x
    n=n//10
print(r)