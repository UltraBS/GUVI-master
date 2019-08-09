n=input()
arr=input().split()
from itertools import permutations
com=list(permutations(arr))
max=0
for i in com:
    print(i)
    num=int("".join(i))
    if max<num:
        max=num
print(max)