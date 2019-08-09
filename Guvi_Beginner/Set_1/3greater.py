x,y,z=[int(x) for x in input().split()]
if x>y and x>z:
  print(x)
elif y>z:
  print(y)
else:
  print(z)
