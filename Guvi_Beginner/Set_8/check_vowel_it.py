st=input()
vow=['a','i','e','o','u','A','E','I','O','U']
c=[x for x in st if x in vow]
if len(c)>0:
    print('yes')
else:
    print('no')