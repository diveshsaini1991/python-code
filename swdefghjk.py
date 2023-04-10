n=int(input())
i=1
while i<=n:
    j=1
    s=ord("A")
    while j<=n-i+1:
        x=(n-(n-i+1))+s
        print(chr(x+j-1),end="")
        j+=1
    print()
    i+=1