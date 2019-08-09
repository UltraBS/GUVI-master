num=int(input())
ssq=0
while(num!=0):
    ssq+=(num%10)**2
    num//=10
print(ssq)