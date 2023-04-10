
def findUnique(arr,n) :
    #Your code goes here
    if n==0:
        return 0
    for x in range(n):
        
        flag=True
        for y in range(n):
            if x==y:
                continue
            if arr[x]==arr[y]:
                flag=False
        
        if flag:
            return arr[x]
        
        

t=int(input())
for c in range(t):
    n= int(input())
    li= [int(p) for p in input().split()]
    print(findUnique(li,n))