li=[[1,2,9],[4,5,6],[7,8,9]]
su=[]
for v in range(2):
    s=0
    if v==0:
        for c in range(len(li)):
            s=s+li[c][c]
        su.append(s)
    else:
        for c in range(len(li)):
                s=s+li[c][len(li)-c-1]
                su.append(s)
print(max(su))

