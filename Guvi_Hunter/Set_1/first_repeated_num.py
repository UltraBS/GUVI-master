n=int(input())
nums=[int(x) for x in input().split()]
for i in nums:
    if(nums.count(i)>1):
        print(i)
        break