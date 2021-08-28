a = list(map(int,input().strip().split()))[:5]

sum=0
for i in range(0,5):
    sum = sum + a[i]
print("Sum of all the numbers is = ",end="")
print(sum)
