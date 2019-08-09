st=list(input())
odpos=[st[x] for x in range(len(st)) if x%2!=0]
evpos=[st[x] for x in range(len(st)) if x%2==0]
print("".join(evpos),''.join(odpos))