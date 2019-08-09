num=int(input())
def divby2(num):
    if num%2==0:
        return divby2(num//2)
    return num
print(divby2(num))