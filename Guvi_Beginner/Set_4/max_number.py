x=[int(x) for x in input().split()]
max=x[0]
for i in x:
    if i>max:
        max=i
print(max)