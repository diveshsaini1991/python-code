li=[[1,2,3,1],[4,5,6,1],[7,8,9,1],[1,2,3,4]]


f=len(li)
sum=[]
for i in range(f):
    d=len(li[i])
    s=0
    for y in range(d):
        s=s+li[y][i]
        sum.append(s)

print(max(sum))

