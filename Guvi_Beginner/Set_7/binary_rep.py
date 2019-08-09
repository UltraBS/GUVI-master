binbin=input()
f=0
for i in binbin:
    if int(i) not in [1,0]:
        print('no')
        f=1
        break
if f==0:
    print('yes')