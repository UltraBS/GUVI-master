n=int(input())
arr=[int(x) for x in input().split()]
m=[]
for i in range(n):
    if i==arr[i]:
        m.append(i)
if(len(m)!=0):
    print(*m)
else:
    print(-1)