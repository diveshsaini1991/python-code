li=[1,2,4,5,7,8,9,6,3]
x=6
# linear search
for i in range(len(li)):
    if x==li[i]:
        print(i)
# binary search
lo=sorted(li)
while True:
    
    o=len(lo)//2
    if lo[o]==x:
        v=lo[o]
        break
    elif x>lo[o]:
        lo=lo[o:]
    else:
        lo=lo[:o]

for i in range(len(li)):
    if v==li[i]:
        print(v,i)


        