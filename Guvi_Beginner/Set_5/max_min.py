n=int(input())
arr=[int(x) for x in input().split()]
min=max=arr[0]
for i in range(n):
    if max<arr[i]:
        max=arr[i]
    elif min>arr[i]:
        min=arr[i]
print(min,max)