li=[[1,2,3],[4,5,6],[7,8,9]]

su=[]

for i in range(len(li)):
    
    su.append(sum(li[i]))

print(max(su))