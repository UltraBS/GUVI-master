h1,m1=[int(x) for x in input().split()]
h2,m2=[int(x) for x in input().split()]
h=h1-h2
m=m1-m2
if m<0:
    m=~m+1
if h<0:
    h=~h+1
print(h,m)