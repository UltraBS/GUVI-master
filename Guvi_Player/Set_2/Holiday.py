d=input()
day={0:['Saturday','Sunday'],1:['Monday','Tuesday','Wednesday','Thursday','Friday']}
holi=['yes','no']
for i in day:
    if d in day[i]:
        print(holi[i])