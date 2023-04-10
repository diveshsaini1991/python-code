n=int(input())

flag=True

for x in range(2,int(n/2)+1):
    if n%x==0:
        flag=False
    if not flag:
        break
if flag:
    print("prime")
else:
    print('not prime')