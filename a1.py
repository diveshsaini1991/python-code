R=int(input("enter no. of rows: "))
C=int(input("enter no. of columns: "))

mat = [[int(input()) for x in range (C)] for y in range(R)]

print(mat)