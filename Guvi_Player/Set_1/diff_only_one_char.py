m,n=input().split()
c=0
for i in range(len(m)):
    if m[i]!=n[i]:
        c+=1
    else:
        continue
if c==1:
    print('yes')
else:
    print('no')