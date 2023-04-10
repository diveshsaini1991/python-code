

n=int(input())
a=2*n
for i in range(a):
    for j in range(a):
        if (j+1)%2!=0 and i%2==0:
            print((2*n)-1,end="")
        elif i==(n*2):
            for v in range((n//2)+1):
                print(n,end="")
        
        else :
            print("   ",end="")
    print()