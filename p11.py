

arr=[1,1,1,2,3,3,4]
arr1=[]
ans=[]
temp=None
for x in arr:
    if temp!=x:
        arr1.append(x)
        temp=x
temp2=None
for x in arr1:
    if temp2!=x:
        ans.append(count(x))
        temp2=x
for x in range(len(arr1)):
    print(arr1[x],ans[x])
