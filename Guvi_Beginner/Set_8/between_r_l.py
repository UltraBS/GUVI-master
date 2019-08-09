num=int(input())
l,r=[int(x) for x in input().split()]
if l<num and num<r:
    print('yes')
else:
    print('no')