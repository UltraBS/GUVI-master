num=input()
number=['1','2','3','4','5','6','7','8','9','0','.']
f=1
for i in num:
    if i in number:
        continue
    else:
        f=0
        print('No')
        break
if f!=0:
    print('Yes')