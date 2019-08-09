s=input()
c=0
for i in s:
    if (i.isalnum()==False):
        c+=1
print(c)