a = list(map(int,input().strip().split()))[:5]

v=a[0:3]
print("sliced list = ",end="")
print(v)
b=a
b[0]=0
b[4]=0
v[0]=0
v[2]=0
print("replaced list-1 = ",end="")
print(b)
print("replaced list-2 = ",end="")
print(v)
