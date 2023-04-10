def swap (arr):
    c=len(arr)
    arr[0],arr[c-1]=arr[c-1],arr[0]
    return arr


# input
n=int(input())
li=[]
for i in range (n):
    li.append(int(input()))


swap(li)
print(li)

