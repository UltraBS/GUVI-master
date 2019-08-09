lis=[int(x) for x in input().split()]
min=lis[0]
for i in lis:
    if min>i:
        min=i
print(min)