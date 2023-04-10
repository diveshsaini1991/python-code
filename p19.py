a=int(input())
i=1
while i<=a:
    s=a
    while s>i:
        print(0,end='')
        s=s-1
    x=1
    while x<=1:
        print(1,end="")
        x=x+1
    y=i-1
    while y>=1:
        print(2,end="")
        y=y-1
    print()
    i=i+1