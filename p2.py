def g (num):
    s=1
    sum=0
    r=1
    while s<=num:
        j=1
        while j<=s:
            sum+=1
            j+=1
        s+=1
    return sum




n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        f=g(i)

        print(f-j+1,end="")
        j+=1
    print()
    i+=1
    