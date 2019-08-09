stringstr=input()

d={}
for i in stringstr:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
    if d[i]==1:
        letter=i
print(letter)