string=list(input())
for i in range(0,len(string),2):
    print(string[i+1]+string[i],end='')