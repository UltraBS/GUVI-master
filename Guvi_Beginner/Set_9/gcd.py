def gcd(num1,num2):
    if num1==num2:
        return num1
    if num1>num2:
        return gcd(num1-num2,num2)
    return gcd(num1,num2-num1)
n,m=[int(x) for x in input().split()]
print(gcd(n,m))