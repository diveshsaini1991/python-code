from sys import stdin

def pairSum(arr, n, x) :
    a=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
               continue
            elif arr[i]+arr[j]==x:
                a=a+1
        print(a)
#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n
#main
t = int(stdin.readline().strip())
while t > 0 :
    arr, n = takeInput()
    x = int(stdin.readline().strip())
    print(pairSum(arr, n, x))
    t -= 1