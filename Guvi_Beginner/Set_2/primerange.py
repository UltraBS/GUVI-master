n,m=[int(x) for x in input().split()]
for num in range(n,m):
  flag=1
  if(num>1):
      for i in range(2,num):
          if(num%i==0):
              flag=0
              break;
      if flag==1:
          print(num,end=' ')
