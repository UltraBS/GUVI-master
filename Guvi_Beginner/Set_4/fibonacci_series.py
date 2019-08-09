num=int(input())
f1=0
f2=1
for i in range(num):
    print(f2,end=' ')
    f3=f2+f1
    f1,f2=f2,f3