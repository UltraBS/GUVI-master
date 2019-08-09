st=input()
l=len(st)
f=0
for i in range(l//2):
    if st[i]!=st[l-i-1]:
        print('no')
        f=1
        break
if f==0:
    print('yes')