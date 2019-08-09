n=int(input())
a=[int(x) for x in input().split()]
m=a[0]
for i in range(n):
    if m>a[i]:
        m=a[i]
print(m)
