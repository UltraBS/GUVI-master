number=int(input())
p=1
while(number!=0):
    p*=(number%10)
    number//=10
print(p)