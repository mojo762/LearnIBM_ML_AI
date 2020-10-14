a=[1,4,8,65,3,2,66,100]
count = 0
length = len(a)
for item in a:
    print(a[count:])
    count = count+1
print(a[:length])
print(a[:(length-1)])
