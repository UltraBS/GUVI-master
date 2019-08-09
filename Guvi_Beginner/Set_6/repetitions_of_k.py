n,k=[int(i) for i in input().split()]
arr=[int(c) for c in input().split()]
r=0
for i in range(n):
    if k==arr[i]:
        r+=1
print(r)