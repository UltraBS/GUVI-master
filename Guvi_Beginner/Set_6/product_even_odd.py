n,m=[int(x) for x in input().split()]
pr=['odd','even']
r=(n%2+m%2)%2
print(pr[r])