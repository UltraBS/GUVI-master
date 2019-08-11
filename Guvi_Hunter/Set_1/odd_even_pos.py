n=int(input())
a=[int(x) for x in input().split()]
for i in range(n):
    if(i%2!=0 and a[i]%2==0):
        print(a[i],end=" ")
    if(i%2==0 and a[i]%2!=0):
        print(a[i],end=" ")