n,c=int(input()),0
nums=[int(x) for x in input().split()]
for i in nums:
    if(nums.count(i)>1):
        print(i)
        c=1
        break
if(c!=1):
    print("unique")
