li=[1,2,4,8,6,7,5,9,3]
lo=[]
for i in range(len(li)):
    x=min(li)
    li.remove(x)
    lo.append(x)

li=lo
print(li)