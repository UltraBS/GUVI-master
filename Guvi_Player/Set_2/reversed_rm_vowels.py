num=int(input())
v=['a','i','e','o','u','A','E','I','O','U']
co=[x for x in input() if x not in v]
co.reverse()
print(''.join(co))