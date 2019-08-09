s=input()
l=[]
f=1
for i in s:
    if i not in l:
        l.append(i)
    else:
        print('No')
        f=0
        break
if f==1:
    print('Yes')