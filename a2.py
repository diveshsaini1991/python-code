from sys import stdin

def findLargest(arr, n, m):
    maxm=[]
    #Your code goes here
    for j in arr:
        maxr=[]
        a=0
        for i in j:
            a=a+i
        maxr.append(a)
    r=max(maxr)
    k=maxr.index(r)
    for h in range(m):
        maxc=[]
        a=0
        for g in arr:
            a+=g[h]
        maxc.append(a)
    c=max(maxc)
    v=maxc.index(c)
    maxm.append(r)
    maxm.append(c)


    main=max(maxm)
    k=maxm.index(main)
    if k==0:
        print("row",k,r)
    else:
        print("column",v,c)

            


























#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())
v=0
while v < t :

    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t += 1