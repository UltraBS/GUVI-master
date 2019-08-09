flag=1
num=int(input())
if(num>1):
    for i in range(2,num//2):
        if(num%i==0):
            print("no")
            flag=0
            break;
if flag==1:
    print('yes')
