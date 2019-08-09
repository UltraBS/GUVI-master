st=input()
l=len(st)
if l%2!=0:
    print(st[:l//2]+'*'+st[l//2+1:])
else:
    print(st[:l//2-1]+'**'+st[l//2+1:])