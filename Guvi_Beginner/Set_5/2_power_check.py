num=int(input())
if num%2==0 or num==1:
    for i in range(0,num//2+1):
        if num==2**i:
            print('yes')
            break
else:
    print('no')
