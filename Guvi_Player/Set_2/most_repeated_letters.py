stringstr=input()
d={}
max,letter=0,''
for i in stringstr:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
    if d[i]>max:
        max,letter=d[i],i
print(letter)
print(type(d))