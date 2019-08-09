n=int(input())
arr=[int(x) for x in input().split()]
un,du=[],[]
for i in arr:
    if i not in un:
        un.append(i)
    elif i not in du:
        du.append(i)
if(len(du)!=0):
    print(*du)
else:
    print("unique")