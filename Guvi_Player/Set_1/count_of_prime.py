l,r=[int(c) for c in input().split()]
c=0
for num in range(l,r+1):
    f = 0
    for i in range(2, num):
        if num % i == 0:
            f = 1
            break
    if f == 0:
        c+=1
print(c)