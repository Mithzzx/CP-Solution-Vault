from collections import defaultdict

times =[[33889,98676],[80071,89737],[44118,52565],[52992,84310],[78492,88209],[21695,67063],[84622,95452],[98048,98856],[98411,99433],[55333,56548],[65375,88566],[55011,62821],[48548,48656],[87396,94825],[55273,81868],[75629,91467]]
targetFriend =6
reg=[]
seats = defaultdict(list)
seats['unoccupied'] = [i for i in range(len(times))]
o=[i for i in range(len(times))]
print(o)

for ind,(a,l) in enumerate(times):
    reg.extend(((ind,a,"a"),(ind,l,"l")))

reg.sort(key=lambda x: x[1])
print(reg)
for ind,time,typ in reg:
    if typ == "a":
        p = seats['unoccupied'].pop(0)
        o[ind] = p
        seats['occupied'].append((p,ind))
        print(ind,time,typ,"u:",seats['unoccupied'],"o:",seats['occupied'])
    if typ == "l":
        if ind == targetFriend:
            print(seats)
            print(o[ind])
            break
        print(ind,o[ind])
        seats['occupied'].pop(o[ind])
        seats['unoccupied'].insert(0,(o[ind]))
        print(ind,time,typ,"u:",seats['unoccupied'],"o:",seats['occupied'])
