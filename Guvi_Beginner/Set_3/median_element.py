n=int(input())
arr=[int(c) for c in input().split()]
arr.sort()
print(arr[n//2])