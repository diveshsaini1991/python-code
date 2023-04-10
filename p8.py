def du (arr):
    x=len(arr)
    for i in range(x):
        for j in range(i,x):
            a=[]
            if i==j:
                continue
            elif arr[i]==arr[j]:
                print(arr[i],end=" ")
                



                




# input
n=int(input())
li=[]
for i in range (n):
    li.append(int(input()))
du(li)
