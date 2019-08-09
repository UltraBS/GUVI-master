num1,o,num2=[x for x in input().split()]
num1=int(num1)
num2=int(num2)
if o=='%':
    print(num1%num2)
elif o=='/':
    print(num1//num2)
elif o=='+':
    print(num1+num2)
elif o=='-':
    print(num1-num2)
elif o=='*':
    print(num1*num2)