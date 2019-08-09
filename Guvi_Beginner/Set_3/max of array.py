number=int(input())
a=[int(q) for q in input().split()]
max=a[0]
for i in range(1,number):
    if max<a[i]:
        max=a[i]
print(max)
