li=[1,5,9,7,3]
lo=[4,8,2,6]

li=sorted(li)
lo=sorted(lo)
for i in lo:
    li.append(i)
li=sorted(li)
print(li)