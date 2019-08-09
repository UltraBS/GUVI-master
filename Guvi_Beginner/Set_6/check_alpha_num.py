st=input()
num=alp=0
for i in st:
    if i.isalpha():
        alp+=1
    elif i.isnumeric():
        num+=1
if num>=1 and alp>=1:
    print('Yes')
else:
    print('No')