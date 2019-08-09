n,k=[int(x) for x in input().split()]
lis=[int(b) for b in input().split()]
for i in range(k):
    lis.insert(0,lis.pop())
print(*lis)