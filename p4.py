def g (num):
    sum=0
    for i in range (1,num+1):
        for j in range (i):
            sum+=1
    return sum



n=int(input())
for i in range (1,n+1):

    for j in range (i):
        x=g(i)
        print(x-j,end="")
    print()
