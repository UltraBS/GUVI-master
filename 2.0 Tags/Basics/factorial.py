n,c=int(input()),0
a=[int(x) for x in input().split()]
for i in a:
	if a.count(i)>=3:
		c+=1
print(c,end="")
