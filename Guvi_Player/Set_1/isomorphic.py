m,n=input().split()
d1,d2={},{}
if len(m)==len(n):
    for i in range(len(n)):
        if m[i] not in d1 or n[i] not in d2:
            d1[m[i]]=1
            d2[n[i]]=1
if len(d1)==len(d2):
    print('yes')
else:
    print('no')