n=int(input())
arr=[int(x) for x in input().split()]
for i in arr:
    if 1==arr.count(i):
        print(i)