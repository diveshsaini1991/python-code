def lar (arr):
    c=len(arr)
    mi=[]
    for i in range(c):
        x=min(arr)
        mi.append(x)
        arr.remove(x)
    return mi




# input
n=int(input())
li=[]
for i in range (n):
    li.append(int(input()))

lo=lar(li)
print (lo[-2])
