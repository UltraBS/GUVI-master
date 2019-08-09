n=int(input())
lis=[int(x) for x in input().split()]
a=sorted(lis)
for i in range(n):
    if a[i]!=lis[i]:
        print(i)
        break